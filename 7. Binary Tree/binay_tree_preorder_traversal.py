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

    #Inorder Traversal
    #Left -> Root -> Right
    def inorder_traversal(self, root):
        if root is None:
            return
        else:
            self.inorder_traversal(root.left)
            print(root.data)
            self.inorder_traversal(root.right)

    #Preorder Traversal
    #Root -> Left -> Right
    def preorder_traversal(self, root):
        if root is None:
            return
        else:
            print(root.data)
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)
            
            

#Use the insert method to add nodes

root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
root.preorder_traversal(root)