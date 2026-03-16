# delete at the end = pop


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

        # edge case 1 (linked list is empty)
        if self.length == 0:
            return None

        # We need two pointers to traverse
        temp = self.head
        pre = self.head

        # normal linkedlist with 2 or more items.
        while temp.next:  # type: ignore # Or while temp.next is not None:
            pre = temp
            temp = temp.next  # type: ignore

        # set the new tail
        self.tail = pre
        self.tail.next = None  # type: ignore
        self.length -= 1

        # edge case 2 (there is only 1 node in linked list)
        if self.length == 0:
            self.head = None
            self.tail = None

        return temp  # Returning the node (OR temp.value if you prefer)


my_linked_list = LinkedList(1)
my_linked_list.append(2)

# my_linked_list.print_list()

# (2) Items - Returns 2 Node
print(my_linked_list.pop())

# (1) Item - Returns 1 Node
print(my_linked_list.pop())

# (0) Items - Returns None
print(my_linked_list.pop())
