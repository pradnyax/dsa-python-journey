# Insert at the end = append


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

        # edge case (when linked list is empty)
        if self.head is None:  # or if self.length == 0:
            self.head = new_node
            self.tail = new_node
        # when items are already present in the linked list
        else:
            self.tail.next = new_node  # type: ignore
            self.tail = new_node

        # increase the length of the linked list by 1.
        self.length += 1


my_linked_list = LinkedList(1)

my_linked_list.append(2)

my_linked_list.print_list()
