#A perfect binary tree is a type of binary tree in which every internal node has exactly two child nodes 
#and all the leaf nodes are at the same level.

class Newnode:
    def __init__(self,data):
        self.data = data
        self.right = self.left = None


def isPerfect(node,d,level=0)