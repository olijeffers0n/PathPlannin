from planning import *

map = Map(20, 20)

for i in range(13):
    map.setNodeBlocked(Node(i,i, None))

finder = AStarPlanner(map, Node(0,1,None), Node(3,5,None))
print(finder.findPath())
