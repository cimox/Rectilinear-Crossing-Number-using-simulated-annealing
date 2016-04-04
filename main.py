import networkx as nx
import matplotlib.pyplot as plt
import random as rand
import copy
import itertools

from Properties import Properties
from Utility import Utility
from Graph import Graph
from Vertex import Vertex


def print_info(str, *args):
    print "[INFO]", str, [arg for arg in args]

def mutate(initialGraph):
    mutatedGraph = copy.copy(initialGraph)

    randPos = rand.randrange(0,initialGraph.number_of_nodes()-1)
    print "randPos",randPos
    node = initialGraph.node(randPos)
    print node[0]['pos']


    return mutatedGraph

if __name__ == "__main__":
    utils = Utility()

    # 1. step: initialize maximum temperature
    T = Properties.Tmax
    print_info('Tmax', T)

    # initialGraph = nx.complete_graph(Properties.Kn_min)
    # printInfo("Initializing graph: [E,V] = ",initialGraph.number_of_nodes(),initialGraph.number_of_edges())
    #
    # #2. step: generate initial random graph
    # fixed_pos = {} # dict w/ positions set
    # for i in range(Properties.Kn_min):
    #     fixed_pos[i] = (rand.uniform(0,1),rand.uniform(0,1)) # random position in (0,1) X and Y
    #     #print "Vertex:", i, "X,Y: ", fixed_pos[i]
    # initialGraph.add_nodes_from(fixed_pos.keys())
    #
    # # add X,Y coordinates to nodes
    # for n,p in fixed_pos.iteritems():
    #     initialGraph.node[n]['pos'] = p
    #     if n == 4:
    #         initialGraph.node[n]['pos'] = 1,1
    # print initialGraph.node
    #
    # pos = nx.spring_layout(initialGraph, pos=fixed_pos, fixed=initialGraph.nodes())
    #
    # nx.draw_networkx(initialGraph, initialGraph.node)
    # plt.show()


    # 2. step: generate initial random graph
    vertices = utils.generate_initial_vertices(Properties.Kn_min)
    # vertices = []
    # vertices.append(Vertex(0.1,0.1))
    # vertices.append(Vertex(0.15,0.45))
    # vertices.append(Vertex(0.35, 0.55))
    # vertices.append(Vertex(0.35, 0.25))
    # vertices.append(Vertex(0.45, 0.4))

    edges = utils.generate_edges(Properties.Kn_min)
    #edgesCombs = itertools.combinations(range(Properties.Kn_min),2)
    g = Graph(vertices,edges) # g is initial randomly generated graph

    g.print_HRF(True, False)
    print g.crossingNumber


    # graph drawing -- START --
    initialGraph = nx.complete_graph(Properties.Kn_min)
    fixed_pos = {}
    vertices = g.get_vertices()
    for i in range(len(vertices)):
        fixed_pos[i] = (vertices[i].x,vertices[i].y)
    fixed_nodes = fixed_pos.keys()
    pos = nx.spring_layout(initialGraph, pos=fixed_pos, fixed=fixed_nodes)
    nx.draw_networkx(initialGraph, pos)
    #if Properties.draw_graph == True:
    #    plt.show()
    # graph drawing -- END --


    # 3. step: loop until stop condition is met
    # stop condition:
    #   - temperature is cooled
    #   - good-enough solution has been found
    neighbor = g.clone() # new and (will be) mutated graph
    neighbor.mutate(True)




























