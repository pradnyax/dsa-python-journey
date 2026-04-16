# add node at the start/head = prepend


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

    def pop(self):

        if self.length == 0:
            return None

        temp = self.head
        pre = self.head

        while temp.next:  # type: ignore # Or while temp.next is not None.
            pre = temp
            temp = temp.next  # type: ignore

        self.tail = pre
        self.tail.next = None  # type: ignore
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

        return temp

    def prepend(self, value):
        new_node = Node(value)  # creates new node

        # case1: LL is empty
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        # case2: LL is not empty
        else:
            new_node.next = self.head  # type: ignore
            self.head = new_node
        self.length += 1
        return True  # NOTE: return True is optional here.


my_linked_list = LinkedList(2)
my_linked_list.append(3)

my_linked_list.prepend(1)

my_linked_list.print_list()
