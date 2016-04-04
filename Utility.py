import copy
import random as rand
from Vertex import Vertex
import itertools
import math

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

    def metropolis_algorithm(self,init,Kmax,T):
        # implementation of metropolis algorithm

        x = copy.copy(init)
        k=0
        while k < Kmax:
            newX=copy.copy(x)
            newX.mutate()

            P = math.exp(-(self.f(newX) - self.f(x))/T)
            if random < P:
                x = newX
            k += 1
        return x

    def f(self,x):
        # fitness function = crossing number of x (graph)

        