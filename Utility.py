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


    def on_segment(self,p,q,r):
        # for given colinear points p, q, r, the function evaluates if point
        # q lies on line segment p-r
        if q.x<=max(p.x,r.x) and q.x>=min(p.x,r.x) and q.y<=max(p.y,r.y) and q.y>=min(p.y,r.y):
            return True
        return False

    def get_orientation(self,p,q,r):
        # returns orientation of ordered triplet of points p, q, r
        # 0 = p, q and r are colinear
        # 1 = clockwise
        # -1 = counterclockwise
        val = (q.y-p.y) * (r.x-q.x) - (q.x-p.x) * (r.y-q.y)
        if val == 0:
            return 0
        return 1 if val > 0 else -1

    def do_intersect(self,p1,q1,p2,q2):
        # returns true if line segment p1-q1 and p2-q2 intersect

        # gets orientation
        o1 = self.get_orientation(p1,q1,p2)
        o2 = self.get_orientation(p1,q1,q2)
        o3 = self.get_orientation(p2,q2,p1)
        o4 = self.get_orientation(p2,q2,q1)

        # general case - intersects in some point on line
        if o1 != o2 and o3 != o4:
            return True

        # special cases
        if o1 == 0 and self.on_segment(p1,p2,q1):
            return True
        if o2 == 0 and self.on_segment(p1,q2,q1):
            return True
        if o3 == 0 and self.on_segment(p2,p1,q2):
            return True
        if o3 == 0 and self.on_segment(p2,q1,q2):
            return True