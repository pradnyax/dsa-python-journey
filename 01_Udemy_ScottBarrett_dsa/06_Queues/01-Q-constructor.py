# Queues ==>  Think of a Queue like a line at a grocery store. The first person to get in line is the first person served.

# a Queue is FIFO => First In, First Out


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):  # constructor
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next


my_q = Queue(4)

my_q.print_queue()


# building a node:
# for my understanding: this node will be identical to a linkedlist/stacks node.
"""
{
"value": 4,
"next": None
}
"""
