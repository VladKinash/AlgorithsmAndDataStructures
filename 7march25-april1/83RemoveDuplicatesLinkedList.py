class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
         
     def delete_duplicate(self):
        uniques = set()
        if self.head is None:
            return
        
        current_node = self.next
        while current_node is not None:
            if current_node.val in uniques:
                self.next = current_node.next
            else:
                uniques.add(current_node.val)
            self = current_node
            current_node = current_node.next
            
        return 
    
