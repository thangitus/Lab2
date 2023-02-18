from DFSGraph import DFSGraph
from Graph import Graph
from bfs import bfs
from dijkstra import dijkstra
from prim import prim

g = Graph()
for i in range(6):
    g.addVertex(i)
u, v = g.addEdge(0, 1, 5)
g.addEdge(0, 5, 2)
g.addEdge(1, 2, 4)
g.addEdge(2, 3, 9)
g.addEdge(3, 4, 7)
g.addEdge(3, 5, 3)
g.addEdge(4, 0, 1)
g.addEdge(5, 4, 8)
g.addEdge(5, 2, 1)
prim(g, u)
sum = 0
for v in g:
    print(v.id, v.pred, v.getDistance())
    sum += v.getDistance()

print(sum)
