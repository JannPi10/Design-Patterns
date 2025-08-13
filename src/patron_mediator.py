from abc import ABC, abstractmethod


class Mediator(ABC):
    @abstractmethod
    def notify(self, sender, event: str):
        pass


class Component:
    def __init__(self, mediator: Mediator = None):
        self.mediator = mediator

    def set_mediator(self, mediator: Mediator):
        self.mediator = mediator


class Button(Component):
    def click(self):
        print("[Button] Click")
        if self.mediator:
            self.mediator.notify(self, "click")


class TextBox(Component):
    def __init__(self, mediator=None):
        super().__init__(mediator)
        self.text = ""

    def input_text(self, text):
        self.text = text
        print(f"[TextBox] Input: {self.text}")


class Checkbox(Component):
    def __init__(self, mediator=None):
        super().__init__(mediator)
        self.checked = False

    def check(self):
        self.checked = not self.checked
        print(f"[Checkbox] Checked: {self.checked}")
        if self.mediator:
            self.mediator.notify(self, "check")


class AuthenticationDialog(Mediator):
    def __init__(self):
        self.title = ""
        self.loginOrRegisterChkBx = Checkbox(self)
        self.loginUsername = TextBox(self)
        self.loginPassword = TextBox(self)
        self.registrationUsername = TextBox(self)
        self.registrationPassword = TextBox(self)
        self.registrationEmail = TextBox(self)
        self.okBtn = Button(self)
        self.cancelBtn = Button(self)

    def notify(self, sender, event: str):
        if sender == self.loginOrRegisterChkBx and event == "check":
            if self.loginOrRegisterChkBx.checked:
                self.title = "Log in"
                print("[Mediator] Modo: Login")
            else:
                self.title = "Register"
                print("[Mediator] Modo: Registro")

        elif sender == self.okBtn and event == "click":
            if self.loginOrRegisterChkBx.checked:
                username = self.loginUsername.text
                password = self.loginPassword.text
                print(f"[Mediator] Intentando login con usuario: {username}")
                found = username == "admin" and password == "1234"
                if not found:
                    print("[Mediator] Error: Usuario no encontrado")
                else:
                    print("[Mediator] Login exitoso")
            else:
                username = self.registrationUsername.text
                email = self.registrationEmail.text
                password = self.registrationPassword.text
                print(f"[Mediator] Registrando nuevo usuario: {username}, Email: {email}")
                print("[Mediator] Registro exitoso e ingreso automático")


if __name__ == "__main__":
    dialog = AuthenticationDialog()

    dialog.loginOrRegisterChkBx.check()
    dialog.loginUsername.input_text("admin")
    dialog.loginPassword.input_text("wrongpass")
    dialog.okBtn.click()

    print("\n---\n")

    dialog.loginOrRegisterChkBx.check()
    dialog.registrationUsername.input_text("newuser")
    dialog.registrationEmail.input_text("new@user.com")
    dialog.registrationPassword.input_text("securepass")
    dialog.okBtn.click()
