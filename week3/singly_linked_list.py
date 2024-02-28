class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def insert_to_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    
    def delete_node(self, value):
        if self.head is None:
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        current_node = self.head
        while current_node.next is not None:
            if current_node.next.data == value:
                break
            current_node = current_node.next

        if current_node.next is None:
            return

        current_node.next = current_node.next.next

        
        
    
        
        
        
new_list = LinkedList()

new_list.insert('Tokyo')
new_list.insert('Rio')
new_list.insert('Prague')
new_list.insert_to_beginning('Athens')

new_list.display()

new_list.delete_node('Rio')

new_list.display()