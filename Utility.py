import plotly.plotly as py
import plotly.graph_objs as go
import random as rand
from Vertex import Vertex
from Properties import Properties
import itertools
import math
import networkx as nx
import matplotlib.pyplot as plt

class Utility:
    'Class w/ utility functions'
    plt.show()

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
            #self.draw_graph(newX) #TODO: animate graph lifecycle

            #P = min(1.0,math.exp(-(self.f(newX) - self.f(x))/T))
            P = min(1.0, math.exp((self.energy(x) - self.energy(newX)) / T))
            if rand.uniform(0,1) < P:
                x = newX
            k += 1
        return x

    def energy(self, x):
        # fitness (penalization) function for a given graph = crossing number of x (graph)

        crossing_number = x.get_crossing_number()

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

    def print_to_graph(self,x_axis,y_T,y_intersections,name):
        # Create a trace
        trace1 = go.Scatter(
            x=x_axis,
            y=[float(i) / max(y_intersections) for i in y_T],
            # y=y_T,
            name='Temperature'
        )
        trace2 = go.Scatter(
            x=x_axis,
            # y=[float(i)/max(y_intersections) for i in y_intersections],
            y=y_intersections,
            name='Fitness'
        )

        data = [trace2]

        layout = go.Layout(
            title='A Simple Plot',
            xaxis=dict(
                title='Generations'
            )
        )
        fig = go.Figure(data=data, layout=layout)
        py.image.save_as(fig, filename=name+'.png')