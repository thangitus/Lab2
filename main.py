from DFSGraph import DFSGraph
from Graph import Graph
from bfs import bfs
from dijkstra import dijkstra
from prim import prim
from topo import Topo
from scc import SCC

# g = Graph()
# for i in range(6):
#     g.addVertex(i)
# u, v = g.addEdge(0, 1, 5)
# g.addEdge(0, 5, 2)
# g.addEdge(1, 2, 4)
# g.addEdge(2, 3, 9)
# g.addEdge(3, 4, 7)
# g.addEdge(3, 5, 3)
# g.addEdge(4, 0, 1)
# g.addEdge(5, 4, 8)
# g.addEdge(5, 2, 1)
# prim(g, u)
# sum = 0
# for v in g:
#     print(v.id, v.pred, v.getDistance())
#     sum += v.getDistance()

# print(sum)

## Demo for Topo
# g = Graph()
# for i in range(7):
#     g.addVertex(i)
    
# g.addEdge(0, 1, 0)
# g.addEdge(0, 3, 0)
# g.addEdge(1, 2, 0)
# g.addEdge(3, 4, 0)
# g.addEdge(6, 3, 0)
# g.addEdge(5, 4, 0)
# g.addEdge(4, 2, 0)

# topo = Topo(g)

# topo.dfs()

# order = topo.get_order()

# for vertex in topo:
#     print(f'Vertex {vertex.getId()} with order : {order[vertex]}')

# print('Topological Order :', [vertex.getId() for vertex in topo.topo[::-1]])


g = Graph()
for i in range(11):
    g.addVertex(i)
    
g.addEdge(0, 1, 0)
g.addEdge(0, 7, 0)
g.addEdge(1, 2, 0)
g.addEdge(2, 3, 0)
g.addEdge(3, 1, 0)
g.addEdge(3, 4, 0)
g.addEdge(4, 5, 0)
g.addEdge(5, 6, 0)
g.addEdge(6, 4, 0)
g.addEdge(7, 8, 0)
g.addEdge(8, 3, 0)
g.addEdge(8, 9, 0)
g.addEdge(9, 10, 0)
g.addEdge(9, 7, 0)
g.addEdge(10, 7, 0)

scc = SCC(g)

scc.dfs()

print(scc.scc)