import plotly.plotly as py
import plotly.graph_objs as go
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
    y_T = []
    y_intersections = []
    while T > Properties.Tmin:
        # TODO: all graphs
        y_T.append(T)
        y_intersections.append(g.crossingNumber)

        if g.get_crossing_number() == Properties.Min_CrossingNumber[Properties.Kn_min]:
            break
        total_iterations += Properties.Kmax

        # simulated annealing core
        g = utils.metropolis_algorithm(g, Properties.Kmax, T)
        T = Properties.alpha * T  # cooldown system - slowly cooling down the system

        #print "[INFO] temp", T, "iter", total_iterations, "cross", g.get_crossing_number()

    g.print_HRF(True, True)
    print "> crossing number", g.get_crossing_number()
    print "[INFO] total iterations", total_iterations
    # utils.draw_graph(g)


    # initialise graph to visualize program run
    stop = total_iterations*Properties.Kmax
    x_axis = np.linspace(0, stop*Properties.Kmax, total_iterations)

    # Create a trace
    trace1 = go.Scatter(
        x=x_axis,
        y=[float(i)/max(y_intersections) for i in y_T],
        #y=y_T,
        name='Temperature'
    )
    trace2 = go.Scatter(
        x=x_axis,
        #y=[float(i)/max(y_intersections) for i in y_intersections],
        y=y_intersections,
        name='Fitness'
    )

    data = [trace2]

    layout = go.Layout(
        title='A Simple Plot',
        xaxis=dict(
            title='Generations'
        )
    )
    fig = go.Figure(data=data, layout=layout)
    py.image.save_as(fig, filename='a-simple-plot.png')

if __name__ == "__main__":
    main()