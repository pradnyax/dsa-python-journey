# Binary Search Tree: "divide and conquer" -> O(logn)

"""
{
"value": 4,
"left":  None,
"right": None
}
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    """def __init__(self, value):
    new_node = Node(value)
    self.root = new_node"""

    def __init__(self):
        self.root = None


my_tree = BinarySearchTree()

print(my_tree.root)


# Output: None
