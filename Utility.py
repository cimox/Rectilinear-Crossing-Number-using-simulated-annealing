import copy
from Properties import Properties
import random as rand
from Vertex import Vertex
import itertools
import networkx as nx

class Utility:
    'Class w/ utility functions'

    def __init__(self):
        self = self

    def generateInitialVertices(self,Kn):
        # generate random vertices at position X,Y
        vertices = []

        for i in range(Kn):
            vertices.append(Vertex(rand.uniform(0,1),rand.uniform(0,1))) # X,Y

        return vertices

    def generateEdges(self,n):
        # returns edges as a combination
        if n > 1:
            edges=itertools.combinations(range(n),2)

        return edges