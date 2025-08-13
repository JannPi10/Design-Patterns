class Editor:
    def __init__(self):
        self.text = ""
        self.curX = 0
        self.curY = 0
        self.selectionWidth = 0

    def set_text(self, text):
        self.text = text

    def set_cursor(self, x, y):
        self.curX = x
        self.curY = y

    def set_selection_width(self, width):
        self.selectionWidth = width

    def create_snapshot(self):
        return Snapshot(self, self.text, self.curX, self.curY, self.selectionWidth)

    def __str__(self):
        return f"[Editor] Text: '{self.text}', Cursor: ({self.curX}, {self.curY}), Selection Width: {self.selectionWidth}"


class Snapshot:
    def __init__(self, editor, text, curX, curY, selectionWidth):
        self._editor = editor
        self._text = text
        self._curX = curX
        self._curY = curY
        self._selectionWidth = selectionWidth

    def restore(self):
        self._editor.set_text(self._text)
        self._editor.set_cursor(self._curX, self._curY)
        self._editor.set_selection_width(self._selectionWidth)


class Command:
    def __init__(self, editor: Editor):
        self._editor = editor
        self._backup = None

    def make_backup(self):
        self._backup = self._editor.create_snapshot()
        print("[Command] Backup realizado.")

    def undo(self):
        if self._backup:
            self._backup.restore()
            print("[Command] Estado restaurado desde backup.")
        else:
            print("[Command] No hay backup para restaurar.")


if __name__ == "__main__":
    editor = Editor()
    command = Command(editor)

    editor.set_text("Hola Mundo")
    editor.set_cursor(5, 1)
    editor.set_selection_width(3)

    print(editor)
    command.make_backup()

    editor.set_text("Texto cambiado")
    editor.set_cursor(0, 0)
    editor.set_selection_width(0)

    print(editor)
    command.undo()

    print(editor)
