# dequeue() ==> Removes the item from the "front" of the line.
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
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node  # type: ignore
            self.last = new_node
        self.length += 1

    def dequeue(self):
        # edge case1: queue is empty
        if self.length == 0:
            return None

        # edge case2: queue has 1 item in the queue
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None

        # case3: queue has 2 or more items in the queue
        else:
            self.first = self.first.next  # type: ignore
            temp.next = None  # type: ignore # this removes the node from the queue

        self.length -= 1
        return temp


my_q = Queue(1)

my_q.enqueue(2)

# running dequeue() 3 times here:

# (2) items in queue - Returns 2 node
print(my_q.dequeue())
# (1) item in queue - Returns 1 node
print(my_q.dequeue())
# (0) item in queue - Returns None
print(my_q.dequeue())

# my_q.print_queue()
