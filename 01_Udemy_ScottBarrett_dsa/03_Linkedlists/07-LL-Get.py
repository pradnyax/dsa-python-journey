# get ==> get the required index


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node  # type: ignore
            self.tail = new_node
        self.length += 1

    def get(self, index):
        # edge case1: to see/test that the index is valid
        if index < 0 or index >= self.length:
            return None
        # case2: for a normal LL to get its index
        temp = self.head
        for _ in range(index):
            temp = temp.next  # type: ignore
        return temp
        # return temp.value --> to get tha value in the output.


my_linked_list = LinkedList(0)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)

print(my_linked_list.get(2))

"""
NOTE: here, in the for loop for def get(), we have used _ instead of (i), a variable, like we normally used is because you are only supposed to put a variable there in for loop when you are planning to use it inside the for loop.
Here we are not going to use it inside, so that's why we will use ( _ )
"""
