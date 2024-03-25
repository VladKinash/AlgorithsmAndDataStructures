
#teacher's code
from singly_linked_list import SinglyLinkedList
from faker import Faker

class HashTable:
    size = 10

    def __init__(self) -> None:
        self.hash_table = [None] * self.size

    def get_hash_value(self, s: str) -> int:
        total = 0
        for c in s:
            total += ord(c)
        return total % self.size
    
    def insert(self, s: str) -> None:
        hash_value = self.get_hash_value(s)
        if self.hash_table[hash_value] is None:
            self.hash_table[hash_value] = SinglyLinkedList()
        self.hash_table[hash_value].insert_front(s)

    def display(self):
        for i in range(self.size):
            if self.hash_table[i] is None:
                print("None")
            else:
                self.hash_table[i].display()



#Student code begins here

    def search(self, s: str) -> bool:
        hash_value = self.get_hash_value(s)
        if self.hash_table[hash_value] is None:
            return False
        else:
            node = self.hash_table[hash_value].head
            while node:
                if node.get_element() == s:
                    return True
                node = node.get_next()
            return False

    def remove(self, s: str) -> str:
        hash_value = self.get_hash_value(s)
        if self.hash_table[hash_value] is not None:
            self.hash_table[hash_value].remove(s)
            return "value removed"
        return "value is not in the list"

  #  def restructure(self, size: int) -> None:
   #     hash_table_new = [None] * size
   #     
    #    for i in self.hash_table:
    #        if i is not None:
      #         hash_table_new.insert(i)
        
     #   self.hash_table = hash_table_new



if __name__ == "__main__":
    print("HASH TABLE EXAMPLE")
    names = ["John", "Emma", "Michael", "Sophia", "William", "Olivia", "James", "Ava", "Benjamin", "Isabella"]
    ht = HashTable()
    for i in names:
        ht.insert(i)
    
    ht.display()
    ht.remove('Emma')
    print(ht.search('Emma'))
    
    ht.restructure(10)
    
    ht.display()
