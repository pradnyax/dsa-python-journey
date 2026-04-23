# pop() ==> Removes and returns the item from the top.


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
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top  # type: ignore
            self.top = new_node
        self.height += 1

    def pop(self):
        # case1: stack is empty
        if self.height == 0:
            return None

        # case2: stack is not empty
        temp = self.top
        self.top = self.top.next  # type: ignore
        temp.next = None  # type: ignore
        self.height -= 1
        return temp


my_stack = Stack(7)

my_stack.push(23)
my_stack.push(3)
my_stack.push(11)

print(my_stack.pop(), "\n")

my_stack.print_stack()


""" output: before pop()
11
3
23
7
"""
