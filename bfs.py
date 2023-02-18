from queue import Queue

from Vertex import Vertex


def bfs(start: Vertex):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.put(start)
    while vertQueue.qsize() > 0:
        currentVert = vertQueue.get()
        for nbr in currentVert.getConnections():
            if nbr.getColor() == 'white':
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.put(nbr)
        currentVert.setColor('black')


