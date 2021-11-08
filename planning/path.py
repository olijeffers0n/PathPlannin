from planning.node import Node


class Path:

    def __init__(self) -> None:
        self.path = []

    def add(self, node : Node) -> None:
        self.path.append(node)

    def __repr__(self) -> str:
        stringvar = "Path["
        for node in self.path:
            stringvar += str(node) + ", "
        stringvar += "]"
        return stringvar