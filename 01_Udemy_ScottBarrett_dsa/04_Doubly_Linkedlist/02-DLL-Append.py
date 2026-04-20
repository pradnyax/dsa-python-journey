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

        # case1: if DLL is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # case2: DLL is not empty
        else:
            self.tail.next = new_node  # type: ignore
            new_node.prev = self.tail  # type: ignore
            self.tail = new_node
        self.length += 1
        return True


my_dll = DoublyLinkedList(1)
my_dll.append(2)

my_dll.print_list()

"""
NOTE: we are going to use the append method in insert method later on, ans the insert method requires a boolean to be returned so we are going to return boolean here, (return True), so it can used in the other method.
"""
