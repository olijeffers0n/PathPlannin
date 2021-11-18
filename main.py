from planning import *

def getPath(manager, node1 : Node, node2 : Node, time : int) -> Path:
    path = AStarPlanner(manager, node1, node2, time).findPath()
    for node in path.path:
        manager.addNode(node.x, node.y, path.path.index(node))
    return path

worldmap = Map(20, 20)

for i in range(13):
    worldmap.setNodeBlocked(Node(i,i, None))

manager = PathManager(worldmap)

manager.addNode(5,6,9)
manager.addNode(5,6,11)

grid = [[" " for _ in range(21)] for _ in range(21)]

for key in worldmap.nodes.keys():
    grid[int(key[0])][int(key[1])] = "⬜"



## Setting Up the manager and map


## Getting Path 1

path = getPath(manager, Node(0,1,None), Node(14,6,None), 0)

for element in path.path:
    grid[element.y][element.x] = "#"



## Getting Path 2

path = getPath(manager, Node(0,5,None), Node(20,20,None), 0)

for element in path.path:
    grid[element.y][element.x] = "%"



## Getting path 3

path = getPath(manager, Node(0,5,None), Node(2,0,None), 0)

for element in path.path:
    grid[element.y][element.x] = "@"

    

## Printing the grid

for row in grid:
    print(" ".join(row))

