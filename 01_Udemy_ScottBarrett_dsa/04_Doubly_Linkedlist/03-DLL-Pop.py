class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
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
            new_node.prev = self.tail  # type: ignore
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        """
        # edge case1: DLL is empty
        if self.length == 0:
            return None
        #  edge case2: DLL has 2 or more items/node
        temp = self.tail
        self.tail = self.tail.prev
        self.tail.next = None       # this will break the connection
        temp.prev = None            # complete break now
        self.length -= 1
        # edge case3: DLL has only 1 item
        # NOTE: this self.length ==0 , this is after we decremented the length by 1.
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
        """
        # another way to write pop() code for better readability
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev  # type: ignore
            self.tail.next = None  # type: ignore
            temp.prev = None  # type: ignore
        self.length -= 1
        return temp
        # return temp.value


my_dll = DoublyLinkedList(1)
my_dll.append(2)

# (2) items in DLL - Returns 2 Node
print(my_dll.pop())

# (1) item in DLL - Returns 1 Node
print(my_dll.pop())

# (0) item - Returns None
print(my_dll.pop())

# my_dll.print_list()

""" to test this for my understanding, when we did: return temp.value
Output is:
2
1
None
"""
