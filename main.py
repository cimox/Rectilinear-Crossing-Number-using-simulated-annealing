import random as rand
import copy
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from Properties import Properties
from Utility import Utility
from Graph import Graph


def print_info(str, *args):
    print "[INFO]", str, [arg for arg in args]

if __name__ == "__main__":
    utils = Utility()

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
    # vertices = []
    # vertices.append(Vertex(1.064, -8.144))
    # vertices.append(Vertex(2.017, 0.51))
    # vertices.append(Vertex(9.311, -2.024))
    # vertices.append(Vertex(4.206, -1.107))
    # vertices.append(Vertex(4.108, -2.862))
    print

    # initialise graph
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    ln1, = ax1.plot([], [], 'r-')


    def animate(i):
        xar = []
        yar = []


    # simulated annealing
    total_iterations = 0
    T = Properties.Tmax
    print_info('Tmax', T)
    vertices = utils.generate_initial_vertices(Properties.Kn_min)
    edges = utils.generate_edges(Properties.Kn_min)
    g = Graph(vertices, edges)  # g is initial randomly generated graph
    g.print_HRF(True, False)
    print "> crossing number",g.crossingNumber

    utils.draw_graph(g)


    # 3. step: loop until stop condition is met
    # stop condition:
    #   - temperature is cooled
    #   - good-enough solution has been found
    while T > Properties.Tmin:
        # TODO: all graphs
        if g.get_crossing_number() == Properties.Min_CrossingNumber[Properties.Kn_min]:
            break
        total_iterations += Properties.Kmax

        g = utils.metropolis_algorithm(g,Properties.Kmax,T)
        T = Properties.alpha * T # cooldown system - slowly cooling down the system

        print "[INFO] temp", T, "iter", total_iterations, "cross", g.get_crossing_number()


    g.print_HRF(True, True)
    print "> crossing number", g.get_crossing_number()
    print "[INFO] total iterations", total_iterations
    utils.draw_graph(g)



























