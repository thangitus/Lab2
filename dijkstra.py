from Graph import Graph
from Vertex import Vertex
from queue import PriorityQueue


def dijkstra(graph: Graph, start: Vertex):
    for v in graph:
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
