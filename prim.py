from queue import PriorityQueue

from Graph import Graph
from Vertex import Vertex


class Prim(Graph):
    def __init__(self, graph):
        super().__init__()
        self.graph = graph

    def prim(self, start: Vertex):
        pq = PriorityQueue()
        for v in self:
            v.setDistance(1e9)
            v.setPred(None)
        pq.put(start)
        start.setDistance(0)
        start.setColor('black')
        while pq.qsize() != 0:
            currentVert = pq.get()
            for nextVert in currentVert.getConnections():
                newCost = currentVert.getWeight(nextVert)
                if newCost < nextVert.getDistance() and nextVert.getColor() == 'white':
                    nextVert.setColor('gray')
                    nextVert.setPred(currentVert)
                    nextVert.setDistance(newCost)
                    pq.put(nextVert)
            currentVert.setColor('black')

    def get_total_distance(self) -> int:
        distance = 0
        for v in self:
            distance += v.getDistance()
        return distance

    def __iter__(self):
        return self.graph.__iter__()
