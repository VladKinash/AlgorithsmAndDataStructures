from typing import List, Optional

class node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None


class linked_list:
    def __init__(self) -> None:
        self.head = node()


    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node


    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total+= 1
            cur = cur.next
        return total
    

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)


    def get(self, index):
        if index >= self.length():
            print("error index")
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index: return cur_node.data
            cur_idx+=1


    def erase(self, index):
        if index >= self.length():
            print("error index")
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = last_node.next
            if cur_idx == index: 
                last_node.next = cur_node.next
                return
            cur_idx+= 1
        


# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:



    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            
            if list1.val < list2.val:
                tail.next, list1 = list1, list1.next

            else:
                tail.next, list2 = list2, list2
            
            tail = tail.next

            if list1:
                tail.next = list1
            
            elif list2:
                tail.next = list2 

        return dummy.next    


