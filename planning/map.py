from planning.node import Node


class Map:

    def __init__(self, height, width) -> None:
        self.height = height
        self.width = width

        self.nodes = {}

    def isNodeBlocked(self, node : Node) -> bool:

        try:
            return self.nodes[(node.x,node.y)] != None
        except:
            return False

    def isNodeBlocked(self, x, y) -> bool:

        try:
            return self.nodes[(x,y)] != None
        except:
            return False

    def setNodeBlocked(self, node : Node) -> None:

        self.nodes[(node.x,node.y)] = True

    def nodeIsWalkable(self, node : Node) -> bool:

        return node.x >= 0 and node.x <= self.width and node.y >= 0 and node.y <= self.height


    