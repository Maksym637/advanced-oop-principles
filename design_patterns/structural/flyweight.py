from typing import List


# Intrinsic shared state
class TreeType:
    def __init__(self, name: str, color: str, texture: str):
        self.name = name
        self.color = color
        self.texture = texture

    def draw(self, x: int, y: int):
        print(
            f"Drawing {self.name} tree of color {self.color} with texture {self.texture} at ({x},{y})"
        )


class TreeFactory:
    _tree_types: dict = {}

    @classmethod
    def get_tree_type(cls, name: str, color: str, texture: str) -> TreeType:
        key = (name, color, texture)
        if key not in cls._tree_types:
            print(f"Creating new TreeType: {key}")
            cls._tree_types[key] = TreeType(name, color, texture)

        return cls._tree_types[key]


# Extrinsic state is position
class Tree:
    def __init__(self, x: int, y: int, tree_type: TreeType):
        self.x = x
        self.y = y
        self.tree_type = tree_type

    def draw(self):
        self.tree_type.draw(self.x, self.y)


class Forest:
    def __init__(self):
        self.trees: List[Tree] = []

    def plant_tree(self, x: int, y: int, name: str, color: str, texture: str):
        tree_type = TreeFactory.get_tree_type(name, color, texture)
        tree = Tree(x, y, tree_type)
        self.trees.append(tree)

    def draw(self):
        for tree in self.trees:
            tree.draw()


forest = Forest()

forest.plant_tree(1, 2, "Oak", "Green", "Rough")
forest.plant_tree(5, 7, "Pine", "Dark Green", "Smooth")
forest.plant_tree(10, 2, "Oak", "Green", "Rough")  # Reuses same TreeType

forest.draw()
