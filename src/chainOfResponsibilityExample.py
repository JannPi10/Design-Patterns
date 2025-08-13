from abc import ABC, abstractmethod

class ComponentWithContextualHelp(ABC):
    @abstractmethod
    def show_help(self):
        pass



class Component(ComponentWithContextualHelp):
    def __init__(self, tooltip_text=None):
        self.tooltip_text = tooltip_text
        self.container = None

    def show_help(self):
        if self.tooltip_text:
            print(f"Tooltip: {self.tooltip_text}")
        elif self.container:
            self.container.show_help()



class Container(Component):
    def __init__(self, tooltip_text=None):
        super().__init__(tooltip_text)
        self.children = []

    def add(self, child):
        self.children.append(child)
        child.container = self



class Button(Component):
    pass


class Panel(Container):
    def __init__(self, modal_help_text=None):
        super().__init__()
        self.modal_help_text = modal_help_text

    def show_help(self):
        if self.modal_help_text:
            print(f"Modal Help: {self.modal_help_text}")
        else:
            super().show_help()



class Dialog(Container):
    def __init__(self, wiki_page_url=None):
        super().__init__()
        self.wiki_page_url = wiki_page_url

    def show_help(self):
        if self.wiki_page_url:
            print(f"Opening wiki page: {self.wiki_page_url}")
        else:
            super().show_help()


class Application:
    def create_ui(self):
        self.dialog = Dialog("http://help.example.com")
        panel = Panel("This panel contains form controls.")

        ok_button = Button("This is an OK button.")
        cancel_button = Button()  

        panel.add(ok_button)
        panel.add(cancel_button)
        self.dialog.add(panel)

    def on_f1_key_press(self, component):
        component.show_help()


if __name__ == "__main__":
    app = Application()
    app.create_ui()

    print("\nPresionando F1 sobre OK button:")
    app.on_f1_key_press(app.dialog.children[0].children[0]) 

    print("\nPresionando F1 sobre Cancel button:")
    app.on_f1_key_press(app.dialog.children[0].children[1])  

    print("\nPresionando F1 sobre el Panel:")
    app.on_f1_key_press(app.dialog.children[0])
