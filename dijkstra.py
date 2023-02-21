from typing import List

from Graph import Graph
from Vertex import Vertex
from queue import PriorityQueue


def get_distance(vertex: Vertex) -> int:
    return vertex.distance


class Dijkstra(Graph):
    def __init__(self, graph):
        super().__init__()
        self.graph = graph
        self.start = None

    def dijkstra(self, start: Vertex):
        for v in self:
            v.setDistance(1e9)
            v.setPred(None)
        pq = PriorityQueue()
        start.setDistance(0)
        pq.put(start)
        while pq.qsize() != 0:
            currentVert = pq.get()
            for nextVert in currentVert.getConnections():
                newDist = currentVert.getDistance() + currentVert.getWeight(nextVert)
                if newDist < nextVert.getDistance():
                    nextVert.setDistance(newDist)
                    nextVert.setPred(currentVert)
                    pq.put(nextVert)

    def get_path(self, v: Vertex) -> [int]:
        path = []
        while v.pred is not None:
            path.append(v.pred)
            v = v.pred
        path.reverse()
        return path

    def __iter__(self):
        return self.graph.__iter__()
