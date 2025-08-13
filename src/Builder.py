from abc import ABC, abstractmethod


class Computer:
    def __init__(self):
        self.cpu = None
        self.gpu = None
        self.ram = None

    def __str__(self):
        return f"Computer [CPU={self.cpu}, GPU={self.gpu}, RAM={self.ram}]"


class ComputerBuilder(ABC):
    @abstractmethod
    def set_cpu(self, cpu: str): pass

    @abstractmethod
    def set_gpu(self, gpu: str): pass

    @abstractmethod
    def set_ram(self, ram: str): pass

    @abstractmethod
    def get_result(self) -> Computer: pass


class GamingComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer()

    def set_cpu(self, cpu: str):
        self.computer.cpu = cpu

    def set_gpu(self, gpu: str):
        self.computer.gpu = gpu

    def set_ram(self, ram: str):
        self.computer.ram = ram

    def get_result(self) -> Computer:
        return self.computer


class ComputerDirector:
    def __init__(self, builder: ComputerBuilder):
        self._builder = builder

    def build_gaming_pc(self):
        self._builder.set_cpu("Intel i9")
        self._builder.set_gpu("NVIDIA RTX 4090")
        self._builder.set_ram("32GB DDR5")


if __name__ == "__main__":
    builder = GamingComputerBuilder()
    director = ComputerDirector(builder)
    director.build_gaming_pc()
    pc = builder.get_result()
    print(pc)
