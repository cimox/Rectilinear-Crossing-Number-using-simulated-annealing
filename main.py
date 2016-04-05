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
        avgs_penalized = []
        stds_penalized = []
        for i in range(2): # 0 - withou penalization, 1 - with penalization
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
                    if i == 0: # not penalized
                        g = utils.metropolis_algorithm(g, Properties.Kmax, T, False)
                    else: # penalized
                        g = utils.metropolis_algorithm(g, Properties.Kmax, T, True)
                    T = Properties.alpha * T  # cooldown system - slowly cooling down the system

                    if Properties.debug:
                        print "[INFO] temp", T, "iter", total_iterations, "cross", g.get_crossing_number()

                print "> final crossing number", g.get_crossing_number()
                print "[END] total iterations", total_iterations, "\n----------------------------\n"

                # initialise graph to visualize program run
                #x_axis = np.linspace(0, total_iterations+1, total_iterations/Properties.Kmax+1)
                #tmp = utils.print_to_graph(x_axis,y_T,y_intersections,
                #                     [min(x_axis),max(x_axis)],[1,max(y_intersections)],
                #                     'results/'+str(Kn)+'/exp-'+str(experiment)+'_N-'+str(Kn))

                if i == 0: # not penalized
                    stds.append(np.std(y_intersections))
                    avgs.append(np.average(y_intersections))
                else: # penalized
                    stds_penalized.append(np.std(y_intersections))
                    avgs_penalized.append(np.average(y_intersections))

                if Properties.debug or Kn >= 8:
                    utils.draw_graph(g,Kn)


        x_axis = np.linspace(0, len(stds), len(stds))
        # std - std penalized
        utils.print_to_graph(x_axis, stds, stds_penalized,
                             [min(x_axis),max(x_axis)],[1,max(max(avgs),max(stds))],
                             'results/'+str(Kn)+'/N-'+str(Kn)+'_std-std',
                             xlab='Experiment',ylab='',ln1_title='Standard deviation',
                             ln2_title='Std dev w/ penalization',
                             title='Standard deviation and penalization',normalization=False
                             )
        # average - average penalized
        utils.print_to_graph(x_axis, avgs, avgs_penalized,
                             [min(x_axis), max(x_axis)], [1, max(max(avgs), max(stds))],
                             'results/' + str(Kn) + '/N-' + str(Kn) + '_avg-avg',
                             xlab='Experiment', ylab='', ln1_title='Average fitness',
                             ln2_title='Average f w/ penalization',
                             title='Average fitness and penalization', normalization=False
                             )
        # not penalized
        utils.print_to_graph(x_axis, avgs, stds,
                             [min(x_axis), max(x_axis)], [1, max(max(avgs), max(stds))],
                             'results/' + str(Kn) + '/N-' + str(Kn) + '_avg-std',
                             xlab='Experiment', ylab='', ln1_title='Average fitness',
                             ln2_title='Standard deviation',
                             title='Average fitness and standard deviation', normalization=False
                             )
        # penalized
        utils.print_to_graph(x_axis, avgs_penalized, stds_penalized,
                             [min(x_axis), max(x_axis)], [1, max(max(avgs), max(stds))],
                             'results/' + str(Kn) + '/N-' + str(Kn) + '_avg-std-pen',
                             xlab='Experiment', ylab='', ln1_title='Average fitness',
                             ln2_title='Standard deviation',
                             title='Average fitness and standard deviation\nPENALIZED', normalization=False
                             )

if __name__ == "__main__":
    main()