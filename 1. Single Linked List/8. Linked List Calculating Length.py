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
        
    def count_nodes_iterative(self):
        temp = self.head
        count = 1
        
        while temp.next:
            count+=1
            temp = temp.next
     
        return count
    
    def count_nodes_recursive(self, node):
        if node is None:
            return 0
        return 1+ self.count_nodes_recursive(node.next)
        
        
        
if __name__ == "__main__":
    llist = LinkedList()

    llist.append("A")
    llist.append("B")
    llist.append("C")
    llist.append("D")

    print(llist.count_nodes_iterative())
    print(llist.count_nodes_recursive(llist.head))
    llist.print_list()