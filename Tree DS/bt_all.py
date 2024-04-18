class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        def insert_node(node, value):
            if node is None:
                return TreeNode(value)
            else:
                if value < node.value:
                    node.left = insert_node(node.left, value)
                else:
                    node.right = insert_node(node.right, value)
            return node

        self.root = insert_node(self.root, value)

    def find_leaf_nodes(self):
        def dfs(node):
            if node:
                if not node.left and not node.right:  # Check if it's a leaf node
                    leaf_nodes.append(node.value)
                dfs(node.left)
                dfs(node.right)

        leaf_nodes = []
        dfs(self.root)
        return leaf_nodes

    def max_depth(self):
        def max_depth_recursive(node):
            if node is None:
                return 0
            else:
                left_depth = max_depth_recursive(node.left)
                right_depth = max_depth_recursive(node.right)
                return max(left_depth, right_depth) + 1

        return max_depth_recursive(self.root)

    def search(self, key):
        def search_recursive(node, key):
            if node is None or node.value == key:
                return node

            if node.value < key:
                return search_recursive(node.right, key)
            return search_recursive(node.left, key)

        return search_recursive(self.root, key)

    def delete(self, key):
        def find_min_value_node(node):
            current = node
            while current.left:
                current = current.left
            return current

        def delete_node(node, key):
            if node is None:
                return node

            if key < node.value:
                node.left = delete_node(node.left, key)
            elif key > node.value:
                node.right = delete_node(node.right, key)
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left

                temp = find_min_value_node(node.right)
                node.value = temp.value
                node.right = delete_node(node.right, temp.value)
            return node

        self.root = delete_node(self.root, key)

# Example usage:
tree = BinaryTree()
values = [5, 3, 7, 2, 4, 6, 8]

for value in values:
    tree.insert(value)

print("Leaf nodes:", tree.find_leaf_nodes())
print("Depth of the tree:", tree.max_depth())

# Search for value 4
result = tree.search(4)
if result:
    print("Value 4 found in the tree.")
else:
    print("Value 4 not found in the tree.")

# Delete node with value 3
tree.delete(3)

print("Leaf nodes after deletion:", tree.find_leaf_nodes())



    
    




