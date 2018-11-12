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
        
        #1.insertion in an empty list
        if self.head is None:
            self.head = new_node
            return 
        
        #2.insertion at the end of the linked list
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
            
        last_node.next = new_node
    
if __name__ == "__main__":
    llist = LinkedList()

    llist.append("A")
    llist.append("B")
    llist.append("C")

    llist.print_list()