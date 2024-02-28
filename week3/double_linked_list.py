class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head = None
        
        
    def insert(self, new_data):
        new_node = Node(data=new_data)
        
        new_node.next = self.head
        new_node.prev = None
        
        if self.head is not None:
            self.head.prev = new_node
        
        self.head = new_node
        
    def insert_back(self, new_data):
        new_node = Node(data=new_data)
        last = self.head
    
        new_node.next = None
    
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return
    
        while (last.next is not None):
            last = last.next
    
        last.next = new_node
        new_node.prev = last
        
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()  
        
        
        
            
cities = LinkedList()

cities.insert('Tokyo')
cities.insert('Rio')
cities.insert('Prague')

cities.display()