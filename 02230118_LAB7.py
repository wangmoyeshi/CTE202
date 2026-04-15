# Task 1
class Node:
    """Node class representing an individual element in the tree."""
    def __init__(self, value):
        self.value = value        # Value of the node 
        self.left = None         # Left child reference 
        self.right = None        # Right child reference 

class BinaryTree:
    """BinaryTree class to manage the root node."""
    def __init__(self, root_value=None):
        # Constructor to initialize an empty or pre-populated tree
        if root_value is not None:
            self.root = Node(root_value)
        else:
            self.root = None # Root node reference 

# --- Testing Task 1 ---
if __name__ == "__main__":
    tree = BinaryTree()
    print("Created new Binary Tree")
    print(f"Root: {tree.root}")

# Task 2
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_node=None):
        self.root = root_node

    # 1. Calculate the maximum depth of the tree [cite: 40]
    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    # 2. Count total number of nodes [cite: 41]
    def size(self, node):
        if node is None:
            return 0
        return 1 + self.size(node.left) + self.size(node.right)

    # 3. Count number of leaf nodes [cite: 42]
    def count_leaves(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return self.count_leaves(node.left) + self.count_leaves(node.right)

    # 4. Check if the tree is a full binary tree (0 or 2 children) [cite: 18, 43]
    def is_full_binary_tree(self, node):
        if node is None:
            return True
        if node.left is None and node.right is None:
            return True
        if node.left is not None and node.right is not None:
            return self.is_full_binary_tree(node.left) and self.is_full_binary_tree(node.right)
        return False

    # 5. Check if the tree is a complete binary tree [cite: 19, 44]
    def is_complete_binary_tree(self, node, index, node_count):
        if node is None:
            return True
        if index >= node_count:
            return False
        return (self.is_complete_binary_tree(node.left, 2 * index + 1, node_count) and
                self.is_complete_binary_tree(node.right, 2 * index + 2, node_count))

# --- Testing Task 2 ---
if __name__ == "__main__":
    # Manually creating a perfect/full tree for the example output
    #       1
    #      / \
    #     2   3
    #    / \ / \
    #   4  5 6  7
    root = Node(1)
    root.left, root.right = Node(2), Node(3)
    root.left.left, root.left.right = Node(4), Node(5)
    root.right.left, root.right.right = Node(6), Node(7)
    
    my_tree = BinaryTree(root)
    total_nodes = my_tree.size(my_tree.root)

    print(f"Tree Height: {my_tree.height(my_tree.root)}")
    print(f"Total Nodes: {total_nodes}")
    print(f"Leaf Nodes Count: {my_tree.count_leaves(my_tree.root)}")
    print(f"Is Full Binary Tree: {my_tree.is_full_binary_tree(my_tree.root)}")
    print(f"Is Complete Binary Tree: {my_tree.is_complete_binary_tree(my_tree.root, 0, total_nodes)}")