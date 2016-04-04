class Properties:
    'Class containing all properties of program'
    Tmax = 10000.0 # maximum temperature
    Tmin = 1 # minimum temperature
    alpha = 0.998 # cooling rate
    Kn_max = 10 # max vertices in graph
    Kn_min = 7 # min vertices in graph
    Min_CrossingNumber = {5:1,6:3,7:9,8:19,9:36,10:62} # optimal solution for n vertices graph : crossing number
    sigma = 1 # gaussian sigma
    decimal_points = 5 # float decimal points rounding used in program
    draw_graph = False
    Kmax = 100 # K-max iterations in metropolis alg.
    f_const = 0.048 # penalization constant

    def __init__(self):
        #do nothing
        self = self