class Edge:
    'Common base class for edges'
    edges_count = 0

    def __init__(self, A, B):
        self.A = A # point A as [x,y] cartesian coordinates
        self.B = B # point B as [x,y] cartesian coordinates
        Edge.edges_count += 1

    def get_count(self):
        return Edge.edges_count

    def get_count_HRF(self):
        print "> Total number of edges: " % Edge.edges_count