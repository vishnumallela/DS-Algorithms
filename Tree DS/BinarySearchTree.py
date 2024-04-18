class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def insert(node,key):
    if node is None:
        return node(key)
    if key < node.data:
        node.left = insert(node.left,key)
    else:
        node.right = insert(node.right,key)
    return node


