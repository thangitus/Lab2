from Vertex import Vertex


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key) -> Vertex:
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, weight=0):
        u, v = self.getVertex(f), self.getVertex(t)
        if f not in self.vertList:
            u = self.addVertex(f)
        if t not in self.vertList:
            v = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)
        return u, v

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())
