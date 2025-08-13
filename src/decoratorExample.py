from abc import ABC, abstractmethod
import zlib
import base64



class DataSource(ABC):
    @abstractmethod
    def write_data(self, data: str):
        pass

    @abstractmethod
    def read_data(self) -> str:
        pass



class FileDataSource(DataSource):
    def __init__(self, filename: str):
        self.filename = filename

    def write_data(self, data: str):
        with open(self.filename, "w", encoding="utf-8") as f:
            f.write(data)
        print(f"[FileDataSource] Datos escritos en {self.filename}")

    def read_data(self) -> str:
        with open(self.filename, "r", encoding="utf-8") as f:
            data = f.read()
        print(f"[FileDataSource] Datos leídos desde {self.filename}")
        return data



class DataSourceDecorator(DataSource):
    def __init__(self, source: DataSource):
        self._wrappee = source

    def write_data(self, data: str):
        self._wrappee.write_data(data)

    def read_data(self) -> str:
        return self._wrappee.read_data()



class EncryptionDecorator(DataSourceDecorator):
    def write_data(self, data: str):
        encrypted = base64.b64encode(data.encode("utf-8")).decode("utf-8")
        print("[EncryptionDecorator] Datos encriptados")
        super().write_data(encrypted)

    def read_data(self) -> str:
        data = super().read_data()
        decrypted = base64.b64decode(data.encode("utf-8")).decode("utf-8")
        print("[EncryptionDecorator] Datos desencriptados")
        return decrypted



class CompressionDecorator(DataSourceDecorator):
    def write_data(self, data: str):
        compressed = zlib.compress(data.encode("utf-8"))
        compressed_base64 = base64.b64encode(compressed).decode("utf-8")
        print("[CompressionDecorator] Datos comprimidos")
        super().write_data(compressed_base64)

    def read_data(self) -> str:
        data = super().read_data()
        decompressed = zlib.decompress(base64.b64decode(data)).decode("utf-8")
        print("[CompressionDecorator] Datos descomprimidos")
        return decompressed



class SalaryManager:
    def __init__(self, source: DataSource):
        self.source = source

    def load(self):
        return self.source.read_data()

    def save(self, salary_records: str):
        self.source.write_data(salary_records)



if __name__ == "__main__":

    salary_data = "Empleado1: $1000\nEmpleado2: $1500"


    source = FileDataSource("salary.dat")


    source = EncryptionDecorator(CompressionDecorator(source))


    manager = SalaryManager(source)
    manager.save(salary_data)

    print("\n--- Lectura de datos ---")
    loaded_data = manager.load()
    print("\nDatos finales:\n", loaded_data)
