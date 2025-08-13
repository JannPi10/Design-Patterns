from abc import ABC, abstractmethod


class Command(ABC):
    def __init__(self, app, editor):
        self.app = app
        self.editor = editor
        self.backup = ""

    def save_backup(self):
        self.backup = self.editor.text

    def undo(self):
        self.editor.text = self.backup

    @abstractmethod
    def execute(self) -> bool:
        pass


class CopyCommand(Command):
    def execute(self) -> bool:
        self.app.clipboard = self.editor.get_selection()
        return False


class CutCommand(Command):
    def execute(self) -> bool:
        self.save_backup()
        self.app.clipboard = self.editor.get_selection()
        self.editor.delete_selection()
        return True


class PasteCommand(Command):
    def execute(self) -> bool:
        self.save_backup()
        self.editor.replace_selection(self.app.clipboard)
        return True


class UndoCommand(Command):
    def execute(self) -> bool:
        self.app.undo()
        return False


class CommandHistory:
    def __init__(self):
        self.history = []

    def push(self, command: Command):
        self.history.append(command)

    def pop(self) -> Command:
        return self.history.pop() if self.history else None


class Editor:
    def __init__(self, text=""):
        self.text = text
        self.selection_start = 0
        self.selection_end = len(text)

    def get_selection(self) -> str:
        return self.text[self.selection_start:self.selection_end]

    def delete_selection(self):
        self.text = self.text[:self.selection_start] + self.text[self.selection_end:]
        self.selection_end = self.selection_start

    def replace_selection(self, new_text: str):
        self.delete_selection()
        self.text = (
            self.text[:self.selection_start] + new_text + self.text[self.selection_start:]
        )
        self.selection_end = self.selection_start + len(new_text)


class Application:
    def __init__(self):
        self.clipboard = ""
        self.editors = []
        self.active_editor = None
        self.history = CommandHistory()

    def execute_command(self, command: Command):
        if command.execute():
            self.history.push(command)

    def undo(self):
        command = self.history.pop()
        if command:
            command.undo()


if __name__ == "__main__":
    app = Application()
    editor = Editor("Hola mundo")
    app.active_editor = editor
    app.editors.append(editor)

    print(f"Texto inicial: '{editor.text}'")

    editor.selection_start = 5
    editor.selection_end = len(editor.text)

    app.execute_command(CutCommand(app, editor))
    print(f"Después de cortar: '{editor.text}' (Clipboard: '{app.clipboard}')")

    app.execute_command(PasteCommand(app, editor))
    print(f"Después de pegar: '{editor.text}'")

    app.undo()
    print(f"Después de deshacer: '{editor.text}'")
  
