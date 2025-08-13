from abc import ABC, abstractmethod


class Visitor(ABC):
    @abstractmethod
    def visit_dot(self, dot): pass

    @abstractmethod
    def visit_circle(self, circle): pass

    @abstractmethod
    def visit_rectangle(self, rectangle): pass

    @abstractmethod
    def visit_compound_shape(self, compound_shape): pass

class Shape(ABC):
    @abstractmethod
    def move(self, x, y): pass

    @abstractmethod
    def draw(self): pass

    @abstractmethod
    def accept(self, visitor: Visitor): pass


class Dot(Shape):
    def __init__(self, id_, x, y):
        self.id = id_
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

    def draw(self):
        print(f"Dibujando Dot en ({self.x}, {self.y})")

    def accept(self, visitor: Visitor):
        visitor.visit_dot(self)

class Circle(Dot):
    def __init__(self, id_, x, y, radius):
        super().__init__(id_, x, y)
        self.radius = radius

    def draw(self):
        print(f"Dibujando Circle en ({self.x}, {self.y}) con radio {self.radius}")

    def accept(self, visitor: Visitor):
        visitor.visit_circle(self)

class Rectangle(Shape):
    def __init__(self, id_, x, y, width, height):
        self.id = id_
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def move(self, x, y):
        self.x += x
        self.y += y

    def draw(self):
        print(f"Dibujando Rectangle en ({self.x}, {self.y}) de {self.width}x{self.height}")

    def accept(self, visitor: Visitor):
        visitor.visit_rectangle(self)

class CompoundShape(Shape):
    def __init__(self, id_):
        self.id = id_
        self.children = []

    def add(self, shape: Shape):
        self.children.append(shape)

    def move(self, x, y):
        for child in self.children:
            child.move(x, y)

    def draw(self):
        print(f"Dibujando CompoundShape {self.id} con {len(self.children)} hijos")
        for child in self.children:
            child.draw()

    def accept(self, visitor: Visitor):
        visitor.visit_compound_shape(self)


class XMLExportVisitor(Visitor):
    def visit_dot(self, dot: Dot):
        print(f"<dot><id>{dot.id}</id><x>{dot.x}</x><y>{dot.y}</y></dot>")

    def visit_circle(self, circle: Circle):
        print(f"<circle><id>{circle.id}</id><x>{circle.x}</x><y>{circle.y}</y><radius>{circle.radius}</radius></circle>")

    def visit_rectangle(self, rectangle: Rectangle):
        print(f"<rectangle><id>{rectangle.id}</id><x>{rectangle.x}</x><y>{rectangle.y}</y>"
              f"<width>{rectangle.width}</width><height>{rectangle.height}</height></rectangle>")

    def visit_compound_shape(self, compound_shape: CompoundShape):
        print(f"<compoundShape><id>{compound_shape.id}</id>")
        for child in compound_shape.children:
            child.accept(self)
        print(f"</compoundShape>")


class Application:
    def __init__(self):
        self.all_shapes = []

    def export(self):
        visitor = XMLExportVisitor()
        for shape in self.all_shapes:
            shape.accept(visitor)


if __name__ == "__main__":
    app = Application()

    dot = Dot(1, 10, 20)
    circle = Circle(2, 15, 25, 5)
    rectangle = Rectangle(3, 0, 0, 30, 40)

    compound = CompoundShape(4)
    compound.add(dot)
    compound.add(circle)
    compound.add(rectangle)

    app.all_shapes.append(compound)

    app.export()
