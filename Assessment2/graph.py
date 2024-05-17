from edge import Edge
from edge_interaction import Edge_Interaction
from vertex import Vertex



class Graph:
    def __init__(self, id) -> None:
        self.vertices = {} 
        self.id = id
        
        
    """
    -def add_member(): adds a user to the graph
    -def display(): prints out all the data related to a user
    -def get_followers(), get_who_commented(), get_who_liked(): find users who have done one of these interactions on a profile of the user A
    -def follow(), like(), comment(): makes user A follow/like/comment user B creating an edge
    -def find_influence(): finds influence that user A has on user B by using the formula provided by the assessment
    -def assign_engagement(): keeps relevant data in edges same as in users
    -def shortest_path(): finds the shortest path between two users
    -def find_max_engagement_path(): finds a path between user A and B that would have the most total engagement
    """
        
        
    def add_member(self, id):
            if id in self.vertices: #checks if a vertex(member) is already in the graph
                print("Vertex is already in the graph")
            else:
                vertex = Vertex(id) #creates vertex and adds it to the dictionary
                self.vertices[id] = vertex
                
    def display(self):
        command = input('Do you want to print all edge properties? It can get verbose \n Y or N:    ')
        for v in self.vertices: #accesses the vertices in the dictionary
            vertex = self.vertices[v]
            #prints all values of a vertex
            print(f"Member {v}:")
            print(f"    Follows: {list(vertex.edges.keys())}")
            print(f"    User likes: {list(vertex.like_edge.keys())}")
            print(f"    User comments: {list(vertex.comment_edge.keys())}")
            print(f"    Followers: {self.get_followers(vertex.id)}")
            print(f"    Likes: {vertex.likes}")
            print(f"    Liked by: {self.get_who_liked(vertex.id)}")
            print(f"    Comments: {vertex.comments}")
            print(f"    Commented by: {self.get_who_commented(vertex.id)}")
            print(f"    Engagement: {vertex.engagement}")
            
            if command.lower() == 'y':
                print("Following Edges:")
                for edge in vertex.edges.values():
                    print(f"    From {edge.vertex} to {edge.destination},   Engagement: {edge.engagement}")
                
                print("Like Edges:")
                for edge in vertex.like_edge.values():
                    print(f"    From {edge.vertex} to {edge.destination},   Interactions: {edge.interactions}")
                
                print("Comment Edges:")
                for edge in vertex.comment_edge.values():
                    print(f"    From {edge.vertex} to {edge.destination},   Interactions: {edge.interactions}")
                        
            else:
                print('')
            print(' ')
            print(' ')
        
        
    def get_followers(self, id):
        followers = []
        for vertex in self.vertices.values():
            if id in vertex.edges.keys():  #Checks if the current vertex exists in as a destination in an edge of another vertex
                followers.append(vertex.id)  #If it is, it is added to the followers list
        return followers
        
    """
    The functions get_who_commented and get_who_liked work exactly as get_followers
    """
    
    def get_who_commented(self, id):
        followers = []
        for vertex in self.vertices.values():
            if id in vertex.comment_edge.keys():
                followers.append(vertex.id)
        return followers
    
    def get_who_liked(self, id):
        followers = []
        for vertex in self.vertices.values():
            if id in vertex.like_edge.keys():
                followers.append(vertex.id)
        return followers    
        
    
    def follow(self, ida, idb):
        #if both vertices are present, a new edge is created
        if ida in self.vertices and idb in self.vertices:
            edge = Edge(idb, ida)
            self.vertices[ida].add_edge(idb, edge)
            self.vertices[idb].followers += 1 #new edge is a new following for the member B, the one who is getting followed
        else:
            print("Destination or starting point do not exist")
            
    
    def like(self, ida, idb):
        #if both vertices are present, a new edge is created
        if ida in self.vertices and idb in self.vertices:
            if idb not in list(self.vertices[ida].like_edge.keys()):
                edge = Edge_Interaction(idb, ida)
                self.vertices[ida].add_like(idb, edge)
                self.vertices[idb].likes += 1 #new edge is a new following for the member B, the one who is getting followed
            else:
                for like in self.vertices[ida].like_edge.values():
                    like.interactions += 1
                    self.vertices[idb].likes += 1
        else:
            print("Destination or starting point do not exist")
            
            
    def comment(self, ida, idb):
        #if both vertices are present, a new edge is created
        if ida in self.vertices and idb in self.vertices:
            if idb not in list(self.vertices[ida].comment_edge.keys()):
                edge = Edge_Interaction(idb, ida)
                self.vertices[ida].add_comment(idb, edge)
                self.vertices[idb].comments += 1 #new edge is a new following for the member B, the one who is getting followed
            else:
                for comment in self.vertices[ida].comment_edge.values():
                    comment.interactions += 1
        else:
            print("Destination or starting point do not exist")            

    
    def find_influence(self, ida, idb):
        total_likes = 0
        total_comments = 0
        engagement = 0
        
        if ida in self.vertices and idb in self.vertices:
            vertex_a = self.vertices[ida]
            
            # Calculate total likes and comments from A to B
            total_likes = sum(edge.interactions for edge in vertex_a.like_edge.values() if edge.destination == idb)
            total_comments = sum(edge.interactions for edge in vertex_a.comment_edge.values() if edge.destination == idb)
            
            
            engagement = vertex_a.engagement
        
        if total_likes == 0 and total_comments == 0:
            print(f"User {ida} has never interacted with user {idb}")
            return None
            
        elif engagement <= 0:
            print('Cannot calculate influence since engagement is 0')
            return None
        
        
        return (total_likes + total_comments) / engagement
                
    
    def assign_engagement(self):
        """
        since the values comments, followers, and likes are dynamic, the edges must be updated to have 
        the latest engagement 
        """
        for vertex in self.vertices.values():
            for edge in vertex.edges.values():
                edge.engagement = vertex.engagement  
            vertex.engagement = vertex.calculate_engagement() 
            

      
    def shortest_path(self, start, end):
            """
            It is a BFS (Breadth-First Search) algorithm that finds the shortest path from vertex A to Vertex B
            """

            queue = [(start, [start])]  #Initialize the queue with the starting vertex and its path
            visited = set()  #Initialize a set to keep track of visited vertices

            while queue:
                vertex, path = queue.pop(0)  #get the vertex and its path from the front of the queue

                if vertex == end:
                    return path  #If the vertex is the end vertex and there aren't any more, return path

                if vertex not in visited:
                    visited.add(vertex)  #current member/vertex will be marked as visited

                    # add all unvisited neighbors to the queue
                    for neighbor in self.vertices[vertex].edges.keys():
                        if neighbor not in visited:
                            queue.append((neighbor, path + [neighbor]))

            return None  #if no path is found, return None
    
    
    def find_max_engagement_path(self, start, end):
        """
        DFS - Depth-First Search algorithm was used to find the way of maximum engagement.
        it finds all possible paths and replaces an old path with a new one if its total engagement is bigger
        """

        best_path = []  #a deck that stores an empty list to store the best path
        max_engagement = 0  #engagement is set to 0 in the beginning

        def dfs(current_vertex, end_vertex, path):
            nonlocal best_path, max_engagement
            if current_vertex == end_vertex:
                #if the current vertex is the end vertex, finds the path's total engagement
                total_engagement = sum(self.vertices[v].engagement for v in path)
                if total_engagement > max_engagement:
                    #if the engagement of current path is bigger than the engagement of the old one, replace best_path with the current path variable
                    best_path = path
                    max_engagement = total_engagement
            else:
                #checks all unvisited neighbors 
                for neighbor in self.vertices[current_vertex].edges.keys():
                    if neighbor not in path:
                        #recursively calls function
                        dfs(neighbor, end_vertex, path + [neighbor])

        dfs(start, end, [start])

        if not best_path:
            print("No path available")
        return best_path
