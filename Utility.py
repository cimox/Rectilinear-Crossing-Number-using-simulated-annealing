import plotly
import plotly.graph_objs as go

import random as rand
import itertools
import math
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

from Vertex import Vertex
from Properties import Properties

class Utility:
    'Class w/ utility functions'
    # plt.show()

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

    def metropolis_algorithm(self,Xinit,Kmax,T,penalization=False):
        # implementation of metropolis algorithm

        x = Xinit.clone()
        k=0
        while k < Kmax:
            newX=x.clone()
            newX.mutate(False)
            #self.draw_graph(newX) #TODO: animate graph lifecycle

            #P = min(1.0,math.exp(-(self.f(newX) - self.f(x))/T))
            if penalization == True:
                P = min(1.0, math.exp((self.energy(x,True) - self.energy(newX,True)) / T))
            else:
                P = min(1.0, math.exp((self.energy(x) - self.energy(newX)) / T))
            if rand.uniform(0,1) < P:
                x = newX
            k += 1
        return x

    def penalization(self,x):
        # returns penalization for graph x if coord not in (0,1)
        penalization = 0
        for v in x.get_vertices():
            if (v.x > 1 and v.y > 1) or (v.x < 0 and v.y < 0):
                penalization += 1
        return penalization

    def energy(self, x, penalization=False):
        # fitness (penalization) function for a given graph = crossing number of x (graph)

        crossing_number = x.get_crossing_number()
        if penalization == True:
            crossing_number += self.penalization(x)

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

    def draw_graph(self,g,Kn):
        # draws graph based on graph g from parameter
        # g - graph
        # Kn - graph degree

        initialGraph = nx.complete_graph(Kn)
        fixed_pos = {}
        vertices = g.get_vertices()
        for i in range(len(vertices)):
            fixed_pos[i] = (vertices[i].x, vertices[i].y)
        fixed_nodes = fixed_pos.keys()
        pos = nx.spring_layout(initialGraph, pos=fixed_pos, fixed=fixed_nodes)
        nx.draw_networkx(initialGraph, pos)
        plt.show()

    def print_to_graph(self,x_axis,y_T,y_intersections,x_range,y_range,
                       name,xlab='Generations',ylab='Normalized to (0,1)',
                       ln1_title='Temperature',ln2_title='Fitness',title=None,
                       url=None,normalization=True):
        # prints graph with x-y data to file
        # x_axis - data on x axis
        # y_T - first Y data
        # y_intersections - intersections data or somethings else
        # x_range - x axis range, same w/ y_range
        # name - title of graph
        # xlab,ylab - x/y axis text label
        # ln1/2_label - line 1 and 2 label
        # title - title of graph
        # url - sends to plot.ly


        # Create a trace

        # normalized
        if normalization:
            max_intersect = max(y_intersections)
            temperature = go.Scatter(
                x=x_axis,
                y=[float(i) / max(y_T) for i in y_T],
                name=ln1_title
            )
            intersections = go.Scatter(
                x=x_axis,
                y=[float(i)/max(y_intersections) for i in y_intersections], # normalized
                name=ln2_title
            )
        else:
            max_intersect = max(y_intersections)
            temperature = go.Scatter(
                x=x_axis, y=y_T, name=ln1_title
            )
            intersections = go.Scatter(
                x=x_axis, y=y_intersections, name=ln2_title
            )

        data = [temperature, intersections]

        std = str(np.std(y_intersections))
        avg = str(np.average(y_intersections))
        if title == None:
            title = str.split(name, '-')[2] + ' Vertices' + ', std: ' + std + ', avg: ' + avg,
        layout = go.Layout(
            title=title,
            xaxis=dict(
                title=xlab,
                titlefont=dict(
                    family='Arial, sans-serif',
                    size=18,
                    color='darkgrey'
                ),
                showticklabels=True,
                tickfont=dict(
                    family='Old Standard TT, serif',
                    size=14,
                    color='black'
                ),
                exponentformat='e',
                showexponent='All',
                range=x_range,
            ),
            yaxis=dict(
                title=ylab,
                titlefont=dict(
                    family='Arial, sans-serif',
                    size=18,
                    color='darkgrey'
                ),
                showticklabels=True,
                tickfont=dict(
                    family='Old Standard TT, serif',
                    size=14,
                    color='black'
                ),
                exponentformat='e',
                showexponent='All'
                #,range=y_range
            )
        )
        fig = go.Figure(data=data, layout=layout)
        plotly.offline.plot(fig,filename=name)
        # if url == True:
        #     plot_url = plotly.plot(fig, filename=name)

        return [avg,std]