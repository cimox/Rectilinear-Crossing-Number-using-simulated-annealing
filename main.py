import numpy as np

from Properties import Properties
from Utility import Utility
from Graph import Graph


def print_info(str, *args):
    print "[INFO]", str, [arg for arg in args]

def normalize(x,min,max):
    return (x-min)/(max-min)

def main():
    utils = Utility()


    # run experimens
    for N in range(Properties.Kn_min,Properties.Kn_max):
        for experiment in range(Properties.experiment_limit):
            print "[START] experiment", experiment, "for N",N

            # simulated annealing initialization
            total_iterations = 0
            T = Properties.Tmax
            vertices = utils.generate_initial_vertices(N)
            edges = utils.generate_edges(N)
            g = Graph(vertices, edges)  # g is initial randomly generated graph
            print "> init crossing number", g.crossingNumber

            # utils.draw_graph(g)

            # 3. step: loop until stop condition is met
            # stop condition:
            #   - temperature is cooled
            #   - good-enough solution has been found
            y_T = []
            y_intersections = []
            while T > Properties.Tmin:
                # TODO: all graphs
                y_T.append(T)
                y_intersections.append(g.crossingNumber)

                if g.get_crossing_number() == Properties.Min_CrossingNumber[N]:
                    break
                total_iterations += Properties.Kmax

                # simulated annealing core
                g = utils.metropolis_algorithm(g, Properties.Kmax, T)
                T = Properties.alpha * T  # cooldown system - slowly cooling down the system

                if __debug__:
                    print "[INFO] temp", T, "iter", total_iterations, "cross", g.get_crossing_number()

            print "> final crossing number", g.get_crossing_number()
            print "[END] total iterations", total_iterations

            # initialise graph to visualize program run
            stop = total_iterations * Properties.Kmax
            x_axis = np.linspace(0, stop * Properties.Kmax, total_iterations)
            utils.print_to_graph(x_axis,y_T,y_intersections,
                                 'exp-'+experiment+'_N-'+N)

            if __debug__:
                utils.draw_graph(g)






if __name__ == "__main__":
    main()