import random as rand
import copy
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time


from Properties import Properties
from Utility import Utility
from Graph import Graph


def print_info(str, *args):
    print "[INFO]", str, [arg for arg in args]

def main():
    utils = Utility()


    # simulated annealing initialization
    total_iterations = 0
    T = Properties.Tmax
    print "> T max", T
    vertices = utils.generate_initial_vertices(Properties.Kn_min)
    edges = utils.generate_edges(Properties.Kn_min)
    g = Graph(vertices, edges)  # g is initial randomly generated graph
    g.print_HRF(True, False)
    print "> crossing number", g.crossingNumber

    # utils.draw_graph(g)

    # 3. step: loop until stop condition is met
    # stop condition:
    #   - temperature is cooled
    #   - good-enough solution has been found
    while T > Properties.Tmin:
        # TODO: all graphs
        if g.get_crossing_number() == Properties.Min_CrossingNumber[Properties.Kn_min]:
            break
        total_iterations += Properties.Kmax

        # simulated annealing core
        g = utils.metropolis_algorithm(g, Properties.Kmax, T)
        T = Properties.alpha * T  # cooldown system - slowly cooling down the system

        print "[INFO] temp", T, "iter", total_iterations, "cross", g.get_crossing_number()

    g.print_HRF(True, True)
    print "> crossing number", g.get_crossing_number()
    print "[INFO] total iterations", total_iterations
    # utils.draw_graph(g)

if __name__ == "__main__":
    main()