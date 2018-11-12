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
        
    def delete_node(self, key):
        #two cases
        #Case 1: node to be deleted is head
        cur_node = self.head
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return
        
        #Case 2: node to be deleted is not head
        prev = None
        
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next
            
        #if the key is not present in the list
        if cur_node is None:
            print("The key is not present in the list")
            return
        
        prev.next = cur_node.next
        cur_node = None
            
    
if __name__ == "__main__":
    llist = LinkedList()

    llist.append("A")
    llist.append("B")
    llist.append("C")
    llist.append("D")

    llist.delete_node("B")
    llist.print_list()