from queue import PriorityQueue

from Vertex import Vertex


def prim(G, start: Vertex):
    pq = PriorityQueue()
    for v in G:
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
