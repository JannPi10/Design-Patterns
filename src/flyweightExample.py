class TreeType:
    def __init__(self, name, color, texture):
        self.name = name
        self.color = color
        self.texture = texture

    def draw(self, canvas, x, y):
        print(f"Dibujando {self.name} de color {self.color} con textura '{self.texture}' "
              f"en posición ({x}, {y}) en el lienzo '{canvas}'")


class TreeFactory:
    _tree_types = []

    @staticmethod
    def get_tree_type(name, color, texture):
        
        for t in TreeFactory._tree_types:
            if t.name == name and t.color == color and t.texture == texture:
                return t
        
        tree_type = TreeType(name, color, texture)
        TreeFactory._tree_types.append(tree_type)
        return tree_type


class Tree:
    def __init__(self, x, y, tree_type):
        self.x = x
        self.y = y
        self.type = tree_type

    def draw(self, canvas):
        self.type.draw(canvas, self.x, self.y)


class Forest:
    def __init__(self):
        self.trees = []

    def plant_tree(self, x, y, name, color, texture):
        tree_type = TreeFactory.get_tree_type(name, color, texture)
        tree = Tree(x, y, tree_type)
        self.trees.append(tree)

    def draw(self, canvas):
        for tree in self.trees:
            tree.draw(canvas)



if __name__ == "__main__":
    forest = Forest()
    forest.plant_tree(10, 20, "Roble", "Verde", "Textura1")
    forest.plant_tree(15, 25, "Roble", "Verde", "Textura1") 
    forest.plant_tree(50, 60, "Pino", "Verde Oscuro", "Textura2")

    forest.draw("Lienzo principal")
