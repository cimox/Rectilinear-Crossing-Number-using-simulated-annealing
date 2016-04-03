import random as rand

class Graph:
    'Common base class for graphs'

    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.crossingNumber = self.getCrossingNumber()

    def getCrossingNumber(self):
        #TODO: implement crossing number self of graph

        return 0

    def get_vertex(self,pos):
        # returns vertex from specific position
        if pos < self.number_vertices():
            return self.vertices[pos]
        return 1

    def number_vertices(self):
        # returns amount of vertices
        return len(self.vertices)

    def mutate(self):
        # pick random vertex and mutate it
        randPos = rand.randint(0, self.number_vertices())
        diff_x = rand.gauss(0,1)
        self.vertices[randPos].x += diff_x

        diff_y = rand.gauss(0,1)
        self.vertices[randPos].y += diff_y

    def printHRF(self,vertices,edges):
        # prints graph attributes in human readable format

        if vertices:
            print "Vertices: "
            for v in self.vertices:
                print v.x, v.y

        if edges:
            print "Edges: "
            for e in self.edges:
                print e