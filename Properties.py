class Properties:
    'Class containing all properties of program'
    debug = False

    Tmax = 100000000000.0 # maximum temperature
    # Tmax = 200000.0  # maximum temperature
    Tmin = 1 # minimum temperature
    alpha = 0.99 # cooling rate
    Kn_max = 11 # max vertices in graph
    Kn_min = 10 # min vertices in graph
    Min_CrossingNumber = {5:1,6:3,7:9,8:19,9:36,10:62} # optimal solution for n vertices graph : crossing number
    sigma = 0.1 # gaussian sigma
    decimal_points = 5 # float decimal points rounding used in program
    draw_graph = True
    Kmax = 3 # K-max iterations in metropolis alg.
    f_const = 0.048 # penalization constant
    experiment_limit = 1

    def __init__(self):
        #do nothing
        self = self