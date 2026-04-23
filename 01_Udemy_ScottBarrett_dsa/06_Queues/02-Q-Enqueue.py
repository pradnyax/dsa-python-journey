# Enqueue() ==> Adds an item to the back of the line.
#           ==> O(1)


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

    def enqueue(self, value):
        new_node = Node(value)  # create a new node

        # case1: queue is empty
        if self.first is None:
            self.first = new_node
            self.last = new_node

        # case2: queue is not empty
        else:
            self.last.next = new_node  # type: ignore
            self.last = new_node
        self.length += 1


my_q = Queue(1)

my_q.enqueue(2)

my_q.print_queue()
