from Graph import Graph
from Vertex import Vertex


class Topo(Graph):
    def __init__(self, graph):
        super().__init__()
        self.time = 0
        self.graph = graph
        self.topo = []

    def dfs(self):
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)

        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex)
    
    
    def get_order(self):
        cnt = 0
        order = {}
        for i in range(len(self.topo) - 1, -1, -1):
            cnt += 1
            order[self.topo[i]] = cnt
        return order

    def dfsvisit(self, startVertex: Vertex):
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex)

        self.topo.append(startVertex)

        startVertex.setColor('black')
        self.time += 1
        startVertex.setFinish(self.time)

    def __iter__(self):
        return self.graph.__iter__()