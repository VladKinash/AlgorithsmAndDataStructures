from graph import Graph
import random as r


"""
Functions:
- def users_activity(): is used to randomly generate activity such as likes and comment, each vertex likes and comments the vertices it follows
- def generate_network(): generates network, randomly creates "follow" connections, calls users_activity()
- def test_network(): uses a template made by the author of a project with following connections manually assigned, useful for testing
- def menu(): provides user with a console interface and allows them to interact with the program
- def test_engagement_network(): used to test max engagement path, best test case to use is find the path between 1 and 4 
"""



def users_activity(graph, id):
    """
    This function is used for members of social media to randomly like and comment each other
    """
    vertex = graph.vertices.get(id)
            
    if vertex == None: 
        return None

    """
    users can only like and comment other users that they follow
    the loop goes over the keys to find other users' id
    then the function def like()/def comment() is called to assign a like/comment
    """
    for f in list(vertex.edges.keys()):
        for _ in range(r.randint(0, 7)):
            graph.like(vertex.id, f)
    
    for f in list(vertex.edges.keys()):
        for _ in range(r.randint(0, 4)):
            graph.comment(vertex.id, f)
            
            
            
def generate_network(graph, user_num):
    
    if user_num <= 0:
        print("ERROR: Social network is only possible when there is more than 1 person")
        return None
    
    for i in range(1, user_num):  #this loop creates users 
        graph1.add_member(i)
    for _ in range(user_num*3): #this loop makes user randomly follow each other
        graph.follow(r.randint(1, user_num-1), r.randint(1, user_num-1))
    for i in range(user_num): #this loop calls function which makes each member like or follow one of the members that it follows
        users_activity(graph, i)
        
    
def test_network(graph):
    """
    This is a pre-made network with 6 users, it is used to test program's function
    in a predictable graph
    """
    for i in range(1, 7):
        graph1.add_member(i)
        
        
    graph.follow(6, 5)
    graph.follow(6, 4)
    graph.follow(6, 3)
    graph.follow(6, 1)
    graph.follow(5, 3)
    graph.follow(5, 1)
    graph.follow(4, 3)
    graph.follow(3, 2)
    graph.follow(3, 4)
    graph.follow(2, 3)
    graph.follow(1, 3)
    graph.follow(1, 4)

    for i in range(7):
        users_activity(graph, i)    
    
    
def test_engagement_network(graph):
    """
    this test case creates 4 main nodes, the node 2 and 3 both have a certain engagement but 3's engagement is bigger, thus, the max engagement
    path between 1 and 4 is 1, 3, 4 and not 1, 2, 4 for example
    """
    for i in range(1, 5):
        graph.add_member(i)

    
    graph.follow(3, 4)
    graph.follow(2, 4)
    graph.follow(1, 4)
    graph.follow(1, 3)
    graph.follow(1, 2)
    
    
    graph.add_member(100)
    graph.add_member(101)
    graph.add_member(102)
    graph.add_member(103)
    graph.add_member(104)
    
    graph.follow(100, 3)
    graph.follow(101, 3)
    graph.follow(102, 3)
    graph.follow(104, 2)
    
    graph.like(100, 3)
    graph.like(101, 3)
    graph.like(102, 3)
    graph.like(104, 2)
    
    
    
    graph.like(100, 3)
    graph.like(101, 3)
    graph.like(102, 3)
    graph.like(104, 2)
    
    graph.comment(100, 3)
    graph.comment(101, 3)
    graph.comment(102, 3)
    graph.comment(104, 2) 
   
    

def menu(graph):
    
    while True:
        print()
        print('0. Generate a test  network')
        print('1. Generate Network')
        print('2. Display all data about network')
        print('3. Find shortest path (in the number of steps) between user A and user B')
        print('4. Find the highest engagement path between user A and user B')        
        print('5. Display influence of one user on another')
        print('6. Create test network designed to test max engagement path')
        print("10. Exit")
        command = input("Please enter a number of a function to call it: \n")
        
        
        if command == "0":
            test_network(graph)
            graph.assign_engagement()
            graph.assign_engagement()
        elif command == "1":
            user_num = int(input("Enter the size of the network: "))
            generate_network(graph, user_num)
            graph.assign_engagement()
            graph.assign_engagement()            
        elif command == "2":
            graph.display()
        elif command == "3":
            user_a = int(input("Enter user A ID:    "))
            user_b = int(input("Enter user B ID:    "))
            print(f'\n The shortest path between user A and B is:   {graph.shortest_path(user_a, user_b)}')
        elif command == "4":
            user_a = int(input("Enter user A ID:    "))
            user_b = int(input("Enter user B ID:    "))
            print(f'\n The path of max engagement between user A and B is:  {graph.find_max_engagement_path(user_a, user_b)}')            
        elif command == "5":
            user_a = int(input("Enter user A ID:    "))
            user_b = int(input("Enter user B ID:    "))
            print(f"\n The influence of user A on user B is:   {graph.find_influence(user_a, user_b)}")
        elif command == '6':
            test_engagement_network(graph)
            graph.assign_engagement()
            graph.assign_engagement()
        elif command == "10":
            print("Exiting the program.")
            break
        else:
            print("Invalid command. Please try again.")
        
            
                
            
    
    
            
        

if __name__ == "__main__":
    graph1 = Graph('graph1')
    
    menu(graph1)
    
    

