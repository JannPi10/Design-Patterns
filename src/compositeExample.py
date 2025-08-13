from abc import ABC, abstractmethod


class Graphic(ABC):
    @abstractmethod
    def move(self, x, y):
        pass

    @abstractmethod
    def draw(self):
        pass



class Dot(Graphic):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

    def draw(self):
        print(f"Dibujando punto en ({self.x}, {self.y})")



class Circle(Dot):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def draw(self):
        print(f"Dibujando círculo en ({self.x}, {self.y}) con radio {self.radius}")



class CompoundGraphic(Graphic):
    def __init__(self):
        self.children = []

    def add(self, child: Graphic):
        self.children.append(child)

    def remove(self, child: Graphic):
        self.children.remove(child)

    def move(self, x, y):
        for child in self.children:
            child.move(x, y)

    def draw(self):
        print("Dibujando grupo compuesto:")
        for child in self.children:
            child.draw()
        print("Finalizado dibujo del grupo compuesto\n")


class ImageEditor:
    def __init__(self):
        self.all = CompoundGraphic()

    def load(self):
        self.all.add(Dot(1, 2))
        self.all.add(Circle(5, 3, 10))

    def group_selected(self, components):
        group = CompoundGraphic()
        for component in components:
            group.add(component)
            self.all.remove(component)
        self.all.add(group)
        self.all.draw()


if __name__ == "__main__":
    editor = ImageEditor()
    editor.load()


    selected_components = list(editor.all.children)
    editor.group_selected(selected_components)
