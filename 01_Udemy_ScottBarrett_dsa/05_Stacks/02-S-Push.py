# push(value) ==> Adds a new item to the top of the stack.


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)  # create a new node

        # case1: if the stack is empty
        if self.height == 0:
            self.top = new_node

        # case2: there are items in the stack
        else:
            new_node.next = self.top  # type: ignore
            self.top = new_node

        self.height += 1


my_stack = Stack(2)

my_stack.push(1)

my_stack.print_stack()


""" output:
1
2
"""
