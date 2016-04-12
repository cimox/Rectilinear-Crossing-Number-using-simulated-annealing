import numpy as np

from Properties import Properties
from Utility import Utility
from Graph import Graph


def normalize(x, min, max):
    return (x - min) / (max - min)


def main():
    utils = Utility()
    f = open('data.csv', 'w')
    f.write('vertices,penalization,stddev,avg\n')

    # run experimens
    for Kn in range(Properties.Kn_min, Properties.Kn_max):
        all_costs = []
        for i in range(2):  # 0 - without penalization, 1 - with penalization
            for experiment in range(Properties.experiment_limit):
                print "[START] experiment", experiment, "for N", Kn

                # simulated annealing initialization
                total_iterations = 1
                T = Properties.Tmax
                vertices = utils.generate_initial_vertices(Kn)
                edges = utils.generate_edges(Kn)
                g = Graph(vertices, edges)  # g is initial randomly generated graph
                all_costs.append(g.crossingNumber)
                print "> init crossing number", g.crossingNumber

                # utils.draw_graph(g)

                # 3. step: loop until stop condition is met
                # stop condition:
                #   - temperature is cooled
                #   - good-enough solution has been found
                temperatures = []
                intersections = []  # aka fitnesses
                while T > Properties.Tmin:
                    # temperatures.append(T)
                    # intersections.append(g.get_crossing_number())

                    if g.get_crossing_number() == Properties.Min_CrossingNumber[Kn]:
                        break  # end if solution has been found
                    total_iterations += Properties.Kmax

                    # simulated annealing core
                    if i == 0:  # not penalized
                        metropol = utils.metropolis_algorithm(g, Properties.Kmax, T, False)
                    else:  # penalized
                        metropol = utils.metropolis_algorithm(g, Properties.Kmax, T, True)
                    g = metropol[0]  # save new graph
                    metr_run_costs = metropol[1]
                    all_costs.extend(metr_run_costs)

                    T = Properties.alpha * T  # cooldown system - slowly cooling down the system

                    if Properties.debug:
                        print "[INFO] temp", T, "iter", total_iterations, "cross", g.get_crossing_number()

                print "> final crossing number", g.get_crossing_number()
                print "[END] total iterations", total_iterations, "\n----------------------------\n"

            f.write(str(Kn) + ',')
            if i == 0:
                f.write('FALSE,')
            else:
                f.write('TRUE,')
            f.write(str(np.std(all_costs)) + ',' + str(np.average(all_costs)) + '\n')
    f.close()

if __name__ == "__main__":
    main()
