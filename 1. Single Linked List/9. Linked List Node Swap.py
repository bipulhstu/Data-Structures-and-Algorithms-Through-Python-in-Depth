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
        
    def swap_nodes(self, key1, key2):
        if key1 == key2:
            return
        
        #traverse to the key1
        prev_1 = None
        cur_1 = self.head
        while cur_1 and cur_1.data != key1:
            prev_1 = cur_1
            cur_1 = cur_1.next
        
        #traverse to the key2
        prev_2 = None
        cur_2 = self.head
        while cur_2 and cur_2.data != key2:
            prev_2 = cur_2
            cur_2 = cur_2.next
            
        if not cur_1 or not cur_2:
            return
        if prev_1:  #if node1 and node2 are not head node
            prev_1.next = cur_2
        else:  #if node1 or node2 is head node
            self.head = cur_2
            
        if prev_2:  #if node1 and node2 are not head node
            prev_2.next = cur_1
        else:  #if node1 or node2 is head node
            self.head = cur_1
            
        #swapping
        cur_1.next, cur_2.next = cur_2.next, cur_1.next
        
        
        
        
        
if __name__ == "__main__":
    llist = LinkedList()

    llist.append("A")
    llist.append("B")
    llist.append("C")
    llist.append("D")
    
    llist.swap_nodes("D", "B")

    llist.print_list()