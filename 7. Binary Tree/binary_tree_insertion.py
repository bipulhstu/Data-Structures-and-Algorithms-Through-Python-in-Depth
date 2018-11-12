class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
    	#compare the new value with the parent node 
    	#Case 1: if root node is not None
    	if self.data:
    		if data < self.data:
    			if self.left is None:
    				self.left = Node(data)
    			else:
    				self.left.insert(data)

    		if data > self.data:
    			if self.right is None:
    				self.right = Node(data)
    			else:
    				self.right.insert(data)

        #Case 2: if root node is None
        else:
    	    self.data = data


    #print the tree
    def print_tree(self):
        if self.left:
        	self.left.print_tree()
        print(self.data)
        if self.right:
        	self.right.print_tree()

#Use the insert method to add nodes

root = Node(10)
root.insert(6)
root.insert(14)
root.insert(3)
root.print_tree()