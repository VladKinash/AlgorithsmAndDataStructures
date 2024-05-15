class Edge_Interaction:
    def __init__(self, destination, vertex):
        self.destination = destination
        self.vertex = vertex
        self.interactions = 1 #interaction is set to 1 since the moment the edge created, it is because of another user's interaction