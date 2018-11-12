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
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        
    def count_occurences_iterative(self, data):
        count = 0
        cur = self.head
        while cur:
            if cur.data == data:
                count += 1
            cur = cur.next
            
        return count
    
    def count_occurences_recursive(self, node,  data):
        if not node:
            return 0
        if node.data == data:
            return 1+self.count_occurences_recursive(node.next, data)
        else:
            return self.count_occurences_recursive(node.next, data)
        
        
        
llist = LinkedList()
llist.append(1)
llist.append(1)
llist.append(1)
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(1)
llist.append(1)
print(llist.count_occurences_iterative(1))
print(llist.count_occurences_recursive(llist.head, 1))