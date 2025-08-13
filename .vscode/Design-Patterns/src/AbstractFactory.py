from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def paint(self) -> str:
        pass


class Checkbox(ABC):
    @abstractmethod
    def paint(self) -> str:
        pass


class WindowsButton(Button):
    def paint(self) -> str:
        return "Rendering Windows-style Button"


class WindowsCheckbox(Checkbox):
    def paint(self) -> str:
        return "Rendering Windows-style Checkbox"


class MacButton(Button):
    def paint(self) -> str:
        return "Rendering Mac-style Button"


class MacCheckbox(Checkbox):
    def paint(self) -> str:
        return "Rendering Mac-style Checkbox"


class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()


class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()


def render_ui(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    print(button.paint())
    print(checkbox.paint())


if __name__ == "__main__":
    render_ui(WindowsFactory())
    render_ui(MacFactory())
