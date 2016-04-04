class Vertex:
    'Common base class for vertices'
    vertices_count = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        Vertex.vertices_count += 1

    def get_count(self):
        return Vertex.vertices_count

    def get_count_HRF(self):
        return "> Total number of vertices: " % Vertex.vertices_count


