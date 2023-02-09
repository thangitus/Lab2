class Vertex:
    def __init__(self, key):
        self.distance = None
        self.pred = None
        self.finishTime = None
        self.discoveryTime = None
        self.id = key
        self.connectedTo = {}
        self.color = 'white'

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

    def setColor(self, color):
        self.color = color

    def setDiscovery(self, discovery):
        self.discoveryTime = discovery

    def setFinish(self, time):
        self.finishTime = time

    def setPred(self, pred):
        self.pred = pred

    def getColor(self):
        return self.color

    def setDistance(self, distance):
        self.distance = distance

    def getDistance(self):
        return self.distance
