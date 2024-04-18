class Node:
    def __init__(self,data):
        self.data = data
        self.left=self.right =None

def build_tree(arr,index):
    if not arr: return None
    arr_length = len(arr)
    root = None

    if index < arr_length and arr[index] is not None:
        root = Node(arr[index])
        root.left = build_tree(arr,2*index+1)
        root.right = build_tree(arr,2*index+2)
    return root

    
sample = [1,3,4,5,6]

c=build_tree(sample,0)
print(c)

def Print_Tree_pre_order(root):
    if not root :return None
    if root.data:
        print(root.data)
    if root.left:
        Print_Tree_pre_order(root.left)
    if root.right:
        Print_Tree_pre_order(root.right)

Print_Tree_pre_order(c)



