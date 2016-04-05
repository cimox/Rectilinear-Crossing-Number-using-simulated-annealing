import numpy as np

from Properties import Properties
from Utility import Utility
from Graph import Graph

def normalize(x,min,max):
    return (x-min)/(max-min)


def main():
    utils = Utility()


    # run experimens
    for Kn in range(Properties.Kn_min,Properties.Kn_max):
        avgs = []
        stds = []
        all_costs = []
        for i in range(2): # 0 - withou penalization, 1 - with penalization
            for experiment in range(Properties.experiment_limit):
                print "[START] experiment", experiment, "for N",Kn

                # simulated annealing initialization
                total_iterations = 1
                T = Properties.Tmax
                vertices = utils.generate_initial_vertices(Kn)
                edges = utils.generate_edges(Kn)
                g = Graph(vertices, edges)  # g is initial randomly generated graph
                all_costs.append(g.crossingNumber)
                stds.append(np.std(all_costs))
                avgs.append(np.average(all_costs))
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
                    if i == 0: # not penalized
                        metropol = utils.metropolis_algorithm(g, Properties.Kmax, T, False)
                    else: # penalized
                        metropol = utils.metropolis_algorithm(g, Properties.Kmax, T, True)
                    g = metropol[0] # save new graph
                    all_costs.extend(metropol[1])
                    stds.append(np.std(all_costs))
                    avgs.append(np.average(all_costs))
                    T = Properties.alpha * T  # cooldown system - slowly cooling down the system

                    if Properties.debug:
                        print "[INFO] temp", T, "iter", total_iterations, "cross", g.get_crossing_number()

                print "> final crossing number", g.get_crossing_number()
                print "[END] total iterations", total_iterations, "\n----------------------------\n"

                # visualize temp, stddev, avg and fitness
                if experiment == Properties.experiment_limit-1:
                    x_axis = np.linspace(0, total_iterations+1, total_iterations/Properties.Kmax+1)
                    utils.print_to_graph(x_axis,y_T,stds,avgs,all_costs,
                                        [min(x_axis),max(x_axis)],[1,max(y_intersections)],
                                        'results/'+str(Kn)+'/exp-'+str(experiment)+'_N-'+str(Kn),normalization=True)
                if experiment == Properties.experiment_limit - 1:
                    x_axis = np.linspace(0, total_iterations + 1, total_iterations / Properties.Kmax + 1)
                    utils.print_to_graph(x_axis, y_T, stds, avgs, all_costs,
                                         [min(x_axis), max(x_axis)], [1, max(y_intersections)],
                                         'results/' + str(Kn) + '/exp-' + str(experiment) + '_N-' + str(Kn),
                                         normalization=False)
                utils.draw_graph(g,Kn)

if __name__ == "__main__":
    main()