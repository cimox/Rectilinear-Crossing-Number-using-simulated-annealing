class Vertex:
    'Common base class for vertices'
    verticesCount = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        Vertex.verticesCount += 1

    def getCount(self):
        return Vertex.verticesCount

    def getCountHRF(self):
        return "> Total number of vertices: " % Vertex.verticesCount


