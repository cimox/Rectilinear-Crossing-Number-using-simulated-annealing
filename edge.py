class Edge:
    'Common base class for edges'
    edgesCount = 0

    def __init__(self, A, B):
        self.A = A # point A as [x,y] cartesian coordinates
        self.B = B # point B as [x,y] cartesian coordinates
        Edge.edgesCount += 1

    def getCount(self):
        return Edge.edgesCount

    def getCountHRF(self):
        print "> Total number of edges: " % Edge.edgesCount

    def isSymmetric(self):