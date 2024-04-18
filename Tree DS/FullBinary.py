class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    #checking Tree is a Full Binary Tree or not
    # condition -1 : Every Parent Node has either two children or no children

def isFullBinary(node):

    #imp---Tree Empty case is a full Binary Tree
    if node is None:
        return True

    if node.left is None and node.right is None:
        return True

    if node.left and node.right:
        return (isFullBinary(node.left) and isFullBinary(node.right))

    return False


x  = Node(1)
x.left = Node(2)
x.right = Node(3)
x.left.left = Node(4)
x.left.right = Node(5)


print(isFullBinary(x))
