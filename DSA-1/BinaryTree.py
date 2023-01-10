# If the value is lesser than the value of the parent node, it is inserted on the left side;
# otherwise,​ it’s inserted on the right side of the BST.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

    def insert(self, data):
        if data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data)     

        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()

        print(self.data)

        if self.right:
            self.right.PrintTree()

    def search(self, data):
        if data == self.data:
            return "Value found"

        elif data < self.data:
            if self.left:
                return self.left.search(data)
            else:
                return "value not found"
                
        else:
            if self.right:
                return self.right.search(data)
            else:
                return "value not found"





root = Node(2)
root.insert(1)
root.insert(3)
root.PrintTree()
print(root.search(5))