class Node
    def __init__(self,data)
        self.data = data
        self.next = None

class LinkedList
    def __init__(self)
        self.head = None
        
    def PrintList(self)
        temp = self.head
    
        while (temp):
            print (temp.data)
            temp = temp.next
        
if __name__ == __main__
    llist = LinkedList()
    
    llist.head = Node(6)
    second = Node(3)
    third = Node(4)
    
    
    #linked
    llist.head.next = second
    second.next = third
    
    llist.PrintList()