from abc import ABC, abstractmethod
from collections import defaultdict


class EventListener(ABC):
    @abstractmethod
    def update(self, filename: str):
        pass


class EventManager:
    def __init__(self):
        self.listeners = defaultdict(list)

    def subscribe(self, event_type: str, listener: EventListener):
        self.listeners[event_type].append(listener)
        print(f"[EventManager] Suscrito a evento '{event_type}'.")

    def unsubscribe(self, event_type: str, listener: EventListener):
        self.listeners[event_type].remove(listener)
        print(f"[EventManager] Cancelada suscripción a evento '{event_type}'.")

    def notify(self, event_type: str, data: str):
        print(f"[EventManager] Notificando evento '{event_type}' a {len(self.listeners[event_type])} oyentes.")
        for listener in self.listeners[event_type]:
            listener.update(data)


class Editor:
    def __init__(self):
        self.events = EventManager()
        self.file = None

    def open_file(self, path: str):
        self.file = File(path)
        print(f"[Editor] Archivo abierto: {self.file.name}")
        self.events.notify("open", self.file.name)

    def save_file(self):
        if self.file:
            self.file.write()
            self.events.notify("save", self.file.name)


class File:
    def __init__(self, path: str):
        self.name = path

    def write(self):
        print(f"[File] Guardando contenido en {self.name}")


class LoggingListener(EventListener):
    def __init__(self, log_filename: str, message: str):
        self.log_filename = log_filename
        self.message = message

    def update(self, filename: str):
        with open(self.log_filename, "a") as log:
            log.write(self.message.replace("%s", filename) + "\n")
        print(f"[LoggingListener] Escrito en log: {self.message.replace('%s', filename)}")


class EmailAlertsListener(EventListener):
    def __init__(self, email: str, message: str):
        self.email = email
        self.message = message

    def update(self, filename: str):
        print(f"[EmailAlertsListener] Enviando email a {self.email}: {self.message.replace('%s', filename)}")


if __name__ == "__main__":
    editor = Editor()

    logger = LoggingListener("log.txt", "Someone has opened the file: %s")
    editor.events.subscribe("open", logger)

    email_alert = EmailAlertsListener("admin@example.com", "Someone has changed the file: %s")
    editor.events.subscribe("save", email_alert)

    editor.open_file("documento.txt")
    editor.save_file()
