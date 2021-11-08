from planning.path import Path
from .node import Node
from .map import Map

from typing import List
import heapq
import math

class AStarPlanner:

    def __init__(self, map : Map, start_node : Node, end_node : Node) -> None:

        self.map = map
        self.start_node = start_node
        self.end_node = end_node

        self.open = []
        self.closed = []

        self.offsets = [
            (-1,0),
            (1,0),
            (0,-1),
            (0,1)
        ]

    def findPath(self) -> Path:

        heapq.heappush(self.open, (self.getCost(self.start_node), self.start_node))
        self.closed.append(self.start_node)
        
        while len(self.open) != 0:
            
            node = self.open[0][1]
            self.open.pop(0)

            if node.__eq__(self.end_node):
                return self.retracePath(node)

            for neighbour in self.getNeighbours(node):
                if not self.closed.__contains__(neighbour):
                    if (self.map.nodeIsWalkable(neighbour)):
                        heapq.heappush(self.open, (self.getCost(neighbour), neighbour))
                        self.closed.append(neighbour)


    def getNeighbours(self, node : Node) -> List[Node]:

        # List comprehension, terrible readability but makes me feel good about myself
        return [Node(node.x + offset[0], node.y + offset[1], node) for offset in self.offsets if not self.map.isNodeBlocked(node.x + offset[0], node.y + offset[1])]

    def getCost(self, node : Node) -> float:

        # Basic distance function
        return math.sqrt(abs(self.end_node.x - node.x) ** 2 + abs(self.end_node.y - node.y) ** 2)

    def retracePath(self, node : Node) -> Path:

        path = Path()
        currentNode = node

        while True:
            if currentNode == None: 
                break
            path.add(currentNode)
            currentNode = currentNode.parent

        path.path = list(reversed(path.path))

        return path