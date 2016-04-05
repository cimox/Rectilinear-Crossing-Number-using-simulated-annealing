import random as rand
import copy
import itertools
from Utility import Utility
from Properties import Properties

class Graph:
    'Common base class for graphs'
    utils = Utility()

    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.crossingNumber = self.get_crossing_number()

    def clone(self):
        # creates clone of current graph
        clone_vertices = copy.deepcopy(self.vertices)
        clone_edges = itertools.tee(self.edges)[0]
        clone = Graph(clone_vertices,clone_edges)

        return clone


    def get_crossing_number(self):
        # returns count of intersections in graph (self)
        cnt = 0 # counter of intersections
        edges = itertools.combinations(range(len(self.vertices)),2) # copy edges generator so we keep them in graph

        # iterate over all edges
        for p1,q1 in edges:
            v=[]
            for i in range(len(self.vertices)): # generate vertices pairs (edges) to check
                if i != p1 and i != q1:
                    v.append(i)
            edges_to_check=itertools.combinations(v,2)

            for p2,q2 in edges_to_check:
                if p1 == p2 and q1 == q2:
                    # do nothing
                    print "[WARN] same positions",p1,q1,p2,q2
                else:
                    if self.utils.do_intersect(self.vertices[p1],self.vertices[q1],
                                               self.vertices[p2],self.vertices[q2]):
                        cnt += 1 # they do intersect
        self.crossingNumber = cnt/2
        return cnt/2

    # def get_crossing_number(self):
    #     intersections = 0
    #
    #     for i in range(len(self.vertices)):
    #         for j in range(i+1,len(self.vertices)):
    #             intersections += self.utils.do_intersect(self.edges[i].A,self.edges[i].B,
    #                                                      self.edges[j].A, self.edges[j].B)
    #     self.crossingNumber = intersections
    #     return intersections

    def new_edges(edges,last=None):
        if last is None:
            return itertools.combinations(edges)

    def get_vertex(self,pos):
        # returns vertex from specific position
        if pos < self.number_vertices():
            return self.vertices[pos]
        return 1

    def get_vertices(self):
        return self.vertices

    def get_copy_vertices(self):
        # returns copy of vertices
        return copy.copy(self.vertices)

    def number_vertices(self):
        # returns amount of vertices
        return len(self.vertices)

    def mutate(self,debug):
        # pick random vertex and mutate it
        randPos = rand.randint(0, self.number_vertices()-1)
        if debug:
            print "[INFO] mutating"
            print "> vertex:", randPos
            print "> position:", self.vertices[randPos].x, self.vertices[randPos].y

        diff_x = round(rand.gauss(0,Properties.sigma),Properties.decimal_points)
        diff_y = round(rand.gauss(0,Properties.sigma), Properties.decimal_points)

        # self.vertices[randPos].x += diff_x
        # self.vertices[randPos].y += diff_x

        self.vertices[randPos].x = round(1-diff_x * self.vertices[randPos].x, Properties.decimal_points)
        self.vertices[randPos].y = round(1-diff_y * self.vertices[randPos].y, Properties.decimal_points)

    def print_HRF(self, vertices, edges):
        # prints graph attributes in human readable format

        if vertices:
            print "Vertices: "
            for v in self.vertices:
                print v.x, v.y

        if edges:
            print "Edges: "
            for e in self.edges:
                print e