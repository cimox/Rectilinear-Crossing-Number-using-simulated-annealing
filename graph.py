class Graph:
    'Common base class for graphs'

    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.crossingNumber = self.getCrossingNumber()

    def getCrossingNumber(self):
        #TODO: implement crossing number self of graph

        return 0
