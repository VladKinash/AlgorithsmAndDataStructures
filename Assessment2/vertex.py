class Vertex:
    def __init__(self, id) -> None:
        self.id = id
        self.edges = {}
        self.like_edge = {}
        self.comment_edge = {}
        self.followers = 0
        self.likes = 0
        self.comments = 0
        self.engagement = 0
        
        
    def add_edge(self, idb, edge):
        #stores edges in a dictionary
        self.edges[idb] = edge  
    
    def add_like(self, idb, edge):
        #stores edges in a dictionary
        self.like_edge[idb] = edge
    
    def add_comment(self, idb, edge):
        #stores edges in a dictionary
        self.comment_edge[idb] = edge        
        
    def calculate_engagement(self):
        #finds engagement using formula provided by the assessment
        if self.followers != 0:
            return (self.likes + self.comments) / self.followers * 100
        else:
            return 0      