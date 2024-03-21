import random
import time
import numpy as np

class Node:
    """
    Represents a node in a priority queue.

    Attributes:
        data: The data stored in the node.
        priority: The priority of the node.
        next: Reference to the next node in the priority queue.
        prev: Reference to the previous node in the priority queue.
    """

    def __init__(self, data, priority) -> None:
        self.data = data
        self.priority = priority
        self.next = None
        self.prev = None
        
    def __str__(self):
        return str(self.priority) + " " + self.data
     
    

class PriorityQueue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None 
        
    def insert(self, data, priority):
        # Create a new node with the given data and priority
        node = Node(data, priority)
        
        # If the priority queue is empty, the new node is set to both the head and tail
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            iter = self.head
            #Traverse the queue until the correct position is found according to the node's priority
            while iter is not None and iter.priority < priority:
                iter = iter.next
            
            # If the new node has to be inserted at the end of the priority queue
            if iter is None:
                self.tail.next = node 
                node.prev = self.tail 
                self.tail = node
            else:
                # If the new node should be inserted at the beginning of the priority queue
                if iter == self.head:
                    iter.prev = node 
                    node.next = iter 
                    self.head = node
                else: 
                    # If the new node should be inserted in the middle of the priority queue
                    iter.prev.next = node 
                    node.prev = iter.prev 
                    iter.prev = node
                    node.next = iter


    def peek(self):
        """
        Returns the data of the node with the highest priority in the priority queue without removing it unlike the function def remove

        Returns:
            The data of the node with the highest priority, or None if the priority queue is empty
        """
        if self.tail is None:
            return None
        else:
            node = self.tail 
        return node.data

    def remove(self):
        """
        Removes and returns the node with the highest priority from the priority queue.

        Returns:
            The node with the highest priority, or None if the priority queue is empty
        """
        if self.tail is None:
            return None
        elif self.tail == self.head:
            node = self.tail
            self.tail = None
            self.head = None
        else:
            node = self.tail 
            self.tail = self.tail.prev 
            self.tail.next = None
        return node


    def traverse(self):
        """
        iterates through nodes printing their data as in the def __string__ template where 
        """
        iter = self.head
        while iter is not None:
            print(f'Flight {iter}')
            iter = iter.next
            
    def is_empty(self):
        """
        checks whether the queue is empty
        """
        return self.head is None
    
    
def generate_traffic(pq_land, pq_take_off):
    # Generate random numbers for the number of landings, takeoffs, and emergencies
    num_landings = np.random.poisson(lam=0.4)
    num_takeoffs = np.random.poisson(lam=0.4)
    num_emergency = np.random.poisson(lam=0.15)
    
    # Generate random priorities in range of 1-500 and insert landing requests into the landing priority queue
    for _ in range(num_landings):
        land_priority = random.randint(1, 500)
        pq_land.insert("Requests landing", land_priority)
        
    # same as above but for the take off queue
    for _ in range(num_takeoffs):
        take_off_priority = random.randint(1, 500)
        pq_take_off.insert("Requests take off", take_off_priority)
    
    """
    inserts an emergency landing in the landing queue, 
    its given priority 501 so it will be always first in the queue unlike other nodes whose max priority is 500
    """
    for _ in range(num_emergency):
        land_priority = 501
        pq_land.insert("requests emergency landing", land_priority)


import time

def airport_main(qlanding, qtake_off):
    """
    Simulates the operation of an airport control tower
    """
    limit = int(input("Enter a number of iterations:  "))
    counter = 0
    while counter < limit:
        qlanding.traverse()
        qtake_off.traverse()
        #the first check is to see if the landing queue is empty since the landing planes are to land first
        if qlanding.is_empty():
            #the plane is removed from the list after taking off
            node = qtake_off.remove()
            #the if check prevents program from crashing in case of the the queue being empty
            if node is not None:
                #time function allows user to not be overwhelmed and see how the queues function as the program is slowed down
                time.sleep(2)
                print(f'Control: {node.priority} takeoff')
                time.sleep(1)
        else:
            node = qlanding.remove()
            time.sleep(2)
            print(f'Control: {node.priority} land')
            time.sleep(1)
        
        #new planes are randomly added to the queues
        generate_traffic(qlanding, qtake_off)
        
        counter += 1
        
        

if __name__ == "__main__":
    pq_land = PriorityQueue()
    pq_take_off = PriorityQueue()
   
    airport_main(pq_land, pq_take_off)
    