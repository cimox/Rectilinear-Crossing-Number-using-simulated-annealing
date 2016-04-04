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
    for Kn in range(Properties.Kn_min,Properties.Kn_max):
        for experiment in range(Properties.experiment_limit):
            print "[START] experiment", experiment, "for N",Kn

            # simulated annealing initialization
            total_iterations = 1
            T = Properties.Tmax
            vertices = utils.generate_initial_vertices(Kn)
            edges = utils.generate_edges(Kn)
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
                y_intersections.append(g.get_crossing_number())

                if g.get_crossing_number() == Properties.Min_CrossingNumber[Kn]:
                    break
                total_iterations += Properties.Kmax

                # simulated annealing core
                g = utils.metropolis_algorithm(g, Properties.Kmax, T, False)
                T = Properties.alpha * T  # cooldown system - slowly cooling down the system

                if Properties.debug:
                    print "[INFO] temp", T, "iter", total_iterations, "cross", g.get_crossing_number()

            print "> final crossing number", g.get_crossing_number()
            print "[END] total iterations", total_iterations, "\n----------------------------\n"

            # initialise graph to visualize program run
            x_axis = np.linspace(0, total_iterations+1, total_iterations/Properties.Kmax+1)
            utils.print_to_graph(x_axis,y_T,y_intersections,
                                 [min(x_axis),max(x_axis)],[1,max(y_intersections)],
                                 'results/'+str(Kn)+'/exp-'+str(experiment)+'_N-'+str(Kn),True)

            if Properties.debug or Kn >= 8:
                utils.draw_graph(g,Kn)






if __name__ == "__main__":
    main()