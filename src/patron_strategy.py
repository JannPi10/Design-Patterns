from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def execute(self, a: int, b: int) -> int:
        pass


class ConcreteStrategyAdd(Strategy):
    def execute(self, a: int, b: int) -> int:
        return a + b


class ConcreteStrategySubtract(Strategy):
    def execute(self, a: int, b: int) -> int:
        return a - b


class ConcreteStrategyMultiply(Strategy):
    def execute(self, a: int, b: int) -> int:
        return a * b


class Context:
    def __init__(self, strategy: Strategy = None):
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self._strategy = strategy

    def execute_strategy(self, a: int, b: int) -> int:
        if not self._strategy:
            raise Exception("No hay estrategia definida")
        return self._strategy.execute(a, b)


def main():
    print("=== Calculadora Estrategia ===")
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    print("Seleccione la operación (+, -, *): ")
    action = input().strip()

    context = Context()

    if action == "+":
        context.set_strategy(ConcreteStrategyAdd())
    elif action == "-":
        context.set_strategy(ConcreteStrategySubtract())
    elif action == "*":
        context.set_strategy(ConcreteStrategyMultiply())
    else:
        print("Operación no válida")
        return

    result = context.execute_strategy(a, b)
    print(f"Resultado: {result}")


if __name__ == "__main__":
    main()
