class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    #print the tree
    def print_tree(self):
        print(self.data)

root = Node(10)
root.print_tree