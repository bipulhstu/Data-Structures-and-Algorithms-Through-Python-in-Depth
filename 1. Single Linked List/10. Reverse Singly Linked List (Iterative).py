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
        
    #helper function
    def print_helper(self, node, name):
        if node is None:
            print(name + " : None")
        else:
            print(name + ":" + node.data)  
        
     # Function to reverse the linked list 
    def reverse_iterative(self): 
        prev = None
        current = self.head 
        while(current is not None): 
            next = current.next
            current.next = prev 
            
            self.print_helper(prev, "PREV")
            self.print_helper(current, "CUR")
            self.print_helper(next, "NXT")
            print("\n")
            
            prev = current 
            current = next
        self.head = prev 
        
        
        
if __name__ == "__main__":
    llist = LinkedList()

    llist.append("A")
    llist.append("B")
    llist.append("C")
    llist.append("D")
    
    llist.print_list()
    print("After reversing: \n")
    
    llist.reverse_iterative()

    llist.print_list()