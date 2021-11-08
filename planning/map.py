from planning.node import Node


class Map:

    def __init__(self, height, width) -> None:
        self.height = height
        self.width = width

        self.nodes = {}

    def isNodeBlocked(self, node : Node) -> bool:

        try:
            return self.nodes[self.__getMapKey(node)] != None
        except:
            return False

    def isNodeBlocked(self, x, y) -> bool:

        try:
            return self.nodes[self.__getMapKey(Node(x, y, None))] != None
        except:
            return False

    def setNodeBlocked(self, node : Node) -> None:

        self.nodes[self.__getMapKey(node)] = True

    def __getMapKey(self, node : Node):

        return ("(%s,%s)" % (node.x, node.y))

    def nodeIsWalkable(self, node : Node) -> bool:

        return node.x >= 0 and node.x <= self.width and node.y >= 0 and node.y <= self.height


    