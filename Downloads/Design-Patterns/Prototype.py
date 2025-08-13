import copy
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, color: str):
        self.color = color

    @abstractmethod
    def clone(self):
        pass


class Circle(Shape):
    def __init__(self, radius: int, color: str):
        super().__init__(color)
        self.radius = radius

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"Circle [Radius={self.radius}, Color={self.color}]"


class Rectangle(Shape):
    def __init__(self, width: int, height: int, color: str):
        super().__init__(color)
        self.width = width
        self.height = height

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"Rectangle [Width={self.width}, Height={self.height}, Color={self.color}]"


if __name__ == "__main__":
    circle1 = Circle(10, "Red")
    circle2 = circle1.clone()
    circle2.color = "Blue"

    rect1 = Rectangle(5, 8, "Green")
    rect2 = rect1.clone()
    rect2.width = 10

    print(circle1)
    print(circle2)
    print(rect1)
    print(rect2)
