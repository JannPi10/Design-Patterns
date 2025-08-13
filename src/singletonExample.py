import threading

class Database:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):

        raise RuntimeError("Usa get_instance() para obtener la instancia")

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    obj = super().__new__(cls)
                    obj.__init__()
                    cls._instance = obj
        return cls._instance

    def __init__(self):
        self.connection = "Conexión a la base de datos establecida"

    def query(self, sql):

        print(f"[DB QUERY] Ejecutando: {sql} usando {self.connection}")


if __name__ == "__main__":
    db1 = Database.get_instance()
    db1.query("SELECT * FROM usuarios")

    db2 = Database.get_instance()
    db2.query("SELECT * FROM productos")

    print(f"¿Es la misma instancia? {db1 is db2}")
