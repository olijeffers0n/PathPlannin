from planning import *

map = Map(20, 20)

for i in range(13):
    map.setNodeBlocked(Node(i,i, None))

finder = AStarPlanner(map, Node(0,1,None), Node(1,0,None))

path = finder.findPath()
print(path)

grid = [[" " for _ in range(20)] for _ in range(20)]

for element in path.path:
    grid[element.y][element.x] = "#"

for key in map.nodes.keys():
    key = str(key).strip("()").split(",")
    grid[int(key[0])][int(key[1])] = "⬜"

for row in grid:
    print(" ".join(row))
