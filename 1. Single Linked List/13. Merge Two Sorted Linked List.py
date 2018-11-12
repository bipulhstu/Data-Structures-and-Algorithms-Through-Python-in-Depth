class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def print_list(self):
        cur_node = self.head
        
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
            
    def append(self, data):
        #create memory
        new_node = Node(data)
        
        #insertion in an empty linked list
        if self.head is None:
            self.head = new_node
            return 
        
        #insertion at the end of the linked list
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
            
        last_node.next = new_node
        
    #Function to merge two sorted linked list
    def merge_sorted(self, llist):
        p = self.head
        q = llist.head
        s = None
        
        if not p:
            return q
        if not q:
            return p
        
        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
                
            new_head = s #found head
        
        #now loop through two linked list
        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
                
        #while one list ends
        if not p:
            s.next = q
        if not q:
            s.next = p
            
        return new_head
        
        
if __name__ == "__main__":
    llist_1 = LinkedList()    
    llist_2 = LinkedList()

    llist_1.append(1)
    llist_1.append(5)
    llist_1.append(7)
    llist_1.append(9)
    llist_1.append(10)

    llist_2.append(2)
    llist_2.append(3)
    llist_2.append(4)
    llist_2.append(6)
    llist_2.append(8)
    
    print("List_1: ")
    llist_1.print_list()
    print("\n")
    print("List_2: ")
    llist_2.print_list()
    
    #merge
    llist_1.merge_sorted(llist_2)
    print("\nMerged Linked List: ")
    llist_1.print_list()