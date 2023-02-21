from Graph import Graph
from Vertex import Vertex


class SCC(Graph):
    def __init__(self, graph):
        super().__init__()
        self.time = 0
        self.scc = 0
        self.scc_set = []
        self.low = {}
        self.num = {}
        self.deleted = set()
        self.st = []
        self.graph = graph

    def dfs(self):
        for aVertex in self:
            self.num[aVertex] = 0

        for aVertex in self:
            if self.num[aVertex] == 0:
                self.dfsvisit(aVertex)

    def dfsvisit(self, startVertex: Vertex):
        self.num[startVertex] = self.time
        self.low[startVertex] = self.time
        self.time += 1
        self.st.append(startVertex)
        
        for nextVertex in startVertex.getConnections():
            if nextVertex in self.deleted:
                continue
            if (self.num[nextVertex] == 0):
                self.dfsvisit(nextVertex)
                self.low[startVertex] = min(self.low[startVertex], self.low[nextVertex])
            else:
                self.low[startVertex] = min(self.low[startVertex], self.num[nextVertex])
        if (self.low[startVertex] == self.num[startVertex]):
            self.scc += 1
            s = set()
            while True:
                v = self.st.pop()
                self.deleted.add(v)
                s.add(v)
                if v == startVertex:
                    break
            print('scc', [vertex.id for vertex in s])
            self.scc_set.append(s)
                

    def __iter__(self):
        return self.graph.__iter__()
