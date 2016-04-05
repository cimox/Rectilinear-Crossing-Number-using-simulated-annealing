import numpy as np

from Properties import Properties
from Utility import Utility
from Graph import Graph

def normalize(x,min,max):
    return (x-min)/(max-min)


def main():
    utils = Utility()
    # std deviations and averages of experiments for each graph
    # format: graph-degree,penalization [T/F],list(std deviation),list(average)
    fi = f = open('stds-avgs_ITER_8-9.txt', 'w')
    fi.write('graph-degree,penalization,stddev,average\n')

    # run experimens
    for Kn in range(Properties.Kn_min,Properties.Kn_max):
        print "[INFO] running", Kn, "graph"
        for i in range(2): # 0 - withou penalization, 1 - with penalization
            print "> penalization", i
            iters = []
            for experiment in range(Properties.experiment_limit):
                print ">> experiment", experiment
                # print "[START] experiment", experiment, "for N",Kn

                # simulated annealing initialization
                total_iterations = 1
                T = Properties.Tmax
                vertices = utils.generate_initial_vertices(Kn)
                edges = utils.generate_edges(Kn)
                g = Graph(vertices, edges)  # g is initial randomly generated graph
                # print "> init crossing number", g.crossingNumber

                # utils.draw_graph(g,Kn)
                # print "> finding solution..."

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
                    if i == 0: # not penalized
                        g = utils.metropolis_algorithm(g, Properties.Kmax, T, False)
                    else: # penalized
                        g = utils.metropolis_algorithm(g, Properties.Kmax, T, True)
                    T = Properties.alpha * T  # cooldown system - slowly cooling down the system

                    if Properties.debug:
                        print "[INFO] temp", T, "iter", total_iterations, "cross", g.get_crossing_number()

                # print "> final crossing number", g.get_crossing_number()
                # print "[END] \n> total iterations", total_iterations
                # print "> temp", T, "iter", total_iterations, "cross", g.get_crossing_number()
                # print "----------------------------"

                # initialise graph to visualize program run
                # if experiment == Properties.experiment_limit-1 or experiment == 0:
                #     # visualize track of first and last experiment
                #     x_axis = np.linspace(0, total_iterations+1, total_iterations/Properties.Kmax+1)
                #     tmp = utils.print_to_graph(x_axis,y_T,y_intersections,
                #                         [min(x_axis),max(x_axis)],[1,max(y_intersections)],
                #                         'results/'+str(Kn)+'/exp-'+str(experiment)+'_N-'+str(Kn)+'_'+str(i))
                iters.append(total_iterations)
            if i == 0:
                fi.write(str(Kn) + ',' + 'False'
                         + ',' + str(np.std(iters)) + ',' + str(np.average(iters)) + '\n')
            else:
                fi.write(str(Kn) + ',' + 'True'
                         + ',' + str(np.std(iters)) + ',' + str(np.average(iters)) + '\n')
    fi.close()

if __name__ == "__main__":
    main()