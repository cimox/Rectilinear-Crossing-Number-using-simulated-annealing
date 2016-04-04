import copy
import random as rand
from Vertex import Vertex
from Properties import Properties
import itertools
import math
import networkx as nx
import matplotlib.pyplot as plt

class Utility:
    'Class w/ utility functions'

    def __init__(self):
        self = self

    def generate_initial_vertices(self, Kn):
        # generate random vertices at position X,Y
        vertices = []

        for i in range(Kn):
            vertices.append(Vertex(
                round(rand.uniform(0,1),Properties.decimal_points),
                round(rand.uniform(0,1),Properties.decimal_points))) # X,Y

        return vertices

    def generate_edges(self, n):
        # returns edges as a dictionary generator of combinations

        if n > 1:
            edges=itertools.combinations(range(n),2)

        return edges

    def metropolis_algorithm(self,Xinit,Kmax,T):
        # implementation of metropolis algorithm

        x = Xinit.clone()
        k=0
        while k < Kmax:
            newX=x.clone()
            newX.mutate(False)

            P = min(1.0,math.exp((self.f(newX) - self.f(x))/T)) # acceptance function
            ran = abs(rand.gauss(1,1))
            if P > ran: # TODO: edit rand number
                x = newX
            k += 1
        return x

    def f(self,x):
        # fitness (penalization) function for a given graph = crossing number of x (graph)

        crossing_number = x.get_crossing_number()
        # crossing_number = math.pow(crossing_number, 2)

        for v in x.get_vertices():
            if v.x > 1 or v.x < 0 or v.y > 1 or v.y < 0:
                crossing_number -= 1

        return crossing_number + Properties.f_const

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
        if o1 != o2 and o3 != o4: # TODO: vychadzanie z rovnakeho bodu
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

    def draw_graph(self,g):
        # draws graph based on graph g from parameter

        initialGraph = nx.complete_graph(Properties.Kn_min)
        fixed_pos = {}
        vertices = g.get_vertices()
        for i in range(len(vertices)):
            fixed_pos[i] = (vertices[i].x, vertices[i].y)
        fixed_nodes = fixed_pos.keys()
        pos = nx.spring_layout(initialGraph, pos=fixed_pos, fixed=fixed_nodes)
        nx.draw_networkx(initialGraph, pos)
        plt.show()