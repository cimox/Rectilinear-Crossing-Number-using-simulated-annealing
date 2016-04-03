import networkx as nx
import matplotlib.pyplot as plt
import random as rand
import copy
import itertools

from Properties import Properties
from Utility import Utility
from Graph import Graph


def printInfo(str, *args):
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
    printInfo('Tmax',T)

    #initialGraph = nx.complete_graph(Properties.Kn_min)
    #rintInfo("Initializing graph: [E,V] = ",initialGraph.number_of_nodes(),initialGraph.number_of_edges())

    # 2. step: generate initial random graph
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
    # #plt.show()





    #

    # 2. step: generate initial random graph
    vertices = utils.generateInitialVertices(Properties.Kn_min)
    edges = utils.generateEdges(Properties.Kn_min)
    g = Graph(vertices,edges) # g is initial randomly generated graph

    g.printHRF(True,False)


    # 3. step: loop until stop condition is met
    # stop condition:
    #   - temperature is cooled
    #   - good-enough solution has been found
    neighbor = copy.copy(g) # new and (will be) mutated graph
    neighbor.mutate()
    # DEBUG:
    neighbor.printHRF(True,False)


























