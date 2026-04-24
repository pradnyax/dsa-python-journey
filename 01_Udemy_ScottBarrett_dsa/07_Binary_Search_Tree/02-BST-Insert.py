# BST insert(value) --> Adds a node to the tree.
#                   --> Starts at the root and moves Left or Right until it finds an empty spot.


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)

        # case1: empty tree
        if self.root is None:
            self.root = new_node
            return True

        temp = self.root

        while True:
            # case2: if new node is equal to another node in the tree! (which is not possible, duplicates are not allowed in BST!)
            if new_node.value == temp.value:
                return False

            # case3: less than root, go left side
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node  # type: ignore
                    return True
                temp = temp.left  # from here it will loop again

            # case4: greater than root, go right side
            else:
                if temp.right is None:
                    temp.right = new_node  # type: ignore
                    return True
                temp = temp.right  # from here it will loop again


my_tree = BinarySearchTree()  # creates our BST

my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)

print(my_tree.root.value)  # type: ignore
print(my_tree.root.left.value)  # type: ignore
print(my_tree.root.right.value)  # type: ignore
