from dataclasses import dataclass


@dataclass(order=True)
class Node:

    def __init__(self, x, y, parent) -> None:
        self.x = x
        self.y = y
        self.parent = parent

    def __eq__(self, o: object) -> bool:
        
        if isinstance(o, self.__class__):
            return self.x == o.x and self.y == o.y
        return False

    def __repr__(self) -> str:
        return "Node[{}, {}]".format(self.x, self.y)