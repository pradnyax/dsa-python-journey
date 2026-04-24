# contains(value) --> Checks if a value exists.
#                 --> Returns True or False. It's the search in Binary Search Tree. --> O(logn)


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
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node  # type: ignore
                    return True
                temp = temp.left  # from here it will loop again
            else:
                if temp.right is None:
                    temp.right = new_node  # type: ignore
                    return True
                temp = temp.right

    def contains(self, value):
        """# case1: BST is empty
        if self.root is None:
            return False"""

        # case2: BST is not empty
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left

            elif value > temp.value:
                temp = temp.right

            # value is equal to temp.value!
            else:
                return True
        # item is not in the tree
        return False


my_tree = BinarySearchTree()

my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.contains(27))

print(my_tree.contains(17))


""" NOTE: no need of case1 here, since it works the same using the while loop when temp is None! """
