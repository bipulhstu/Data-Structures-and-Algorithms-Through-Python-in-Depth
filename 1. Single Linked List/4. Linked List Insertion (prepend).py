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
        
    def prepend(self, data):
        #create memory
        new_node = Node(data)
            
        #prepend inserts data in the beginning
        new_node.next = self.head  #new node points to the head
        self.head = new_node   #now new node is the head node
            
    
if __name__ == "__main__":
    llist = LinkedList()

    llist.append("A")
    llist.append("B")
    llist.append("C")
    llist.prepend("D")

    llist.print_list()