from planning.map import Map
from collections import defaultdict


class PathManager:

    def __init__(self, map : Map) -> None:
        
        self.map = map
        self.nodes = defaultdict(list)

    def addNode(self, x, y, time) -> None:

        if not self.nodes[time].__contains__((x,y)):
            self.nodes[time].append((x,y))

    def isNodeBlocked(self, x, y, time) -> bool:
        
        return self.map.isNodeBlocked(x,y) or self.nodes[time].__contains__((x,y))
