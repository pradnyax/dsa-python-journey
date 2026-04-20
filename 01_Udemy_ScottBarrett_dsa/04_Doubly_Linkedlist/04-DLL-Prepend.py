# prepend(value) ==> Adds a new node to the very beginning of the list.


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

    def prepend(self, value):
        new_node = Node(value)
        # edge case1: DLL is empty
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        # edge case2: DLL has 1 or more nodes/items.
        else:
            new_node.next = self.head # type: ignore
            self.head.prev = new_node # type: ignore
            self.head = new_node
        self.length += 1
        return True


my_dll = DoublyLinkedList(12)
my_dll.append(13)

my_dll.prepend(11)

my_dll.print_list()
