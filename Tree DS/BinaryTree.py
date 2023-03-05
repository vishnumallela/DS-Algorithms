class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def traversePreOrder(self):
        print(self.data)
        if self.left:
            self.left.traversePreOrder()
        if self.right:
            self.right.traversePreOrder()

    def traverseInorder(self):
        if self.left:
            self.left.traverseInorder()
        print(self.data)
        if self.right:
            self.right.traverseInorder()

    def traversePostOrder(self):
        if self.left:
            self.left.traversePostOrder()
        if self.right:
            self.right.traversePostOrder()
        print(self.data)

root = Node(1)
root.left = Node(2)
root.right = Node(3)

print('Printing inorder')
root.traverseInorder()
print("printing post order")
root.traversePostOrder()
print("printing preorder")
root.traversePreOrder()
            

    