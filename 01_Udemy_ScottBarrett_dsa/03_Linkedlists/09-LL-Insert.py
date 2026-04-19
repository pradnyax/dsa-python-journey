# insert ==> adding a node/item in the LL, at beginning or end or in the middle.


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

    def prepend(self, value):
        new_node = Node(value)  # creates new node

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head  # type: ignore
            self.head = new_node
        self.length += 1
        return True  # NOTE: return True is optional here.

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next  # type: ignore
        return temp

    def insert(self, index, value):
        # edge case1: index is out of range
        if index < 0 or index > self.length:
            return False

        # case2: inserting/adding to the beginning of LL
        if index == 0:
            return self.prepend(value)

        # case3: inserting/adding to the end of LL
        if index == self.length:
            return self.append(value)

        # case4: inserting in the middle of LL
        new_node = Node(value)  # creating new node
        temp = self.get(index - 1)
        new_node.next = temp.next  # type: ignore
        temp.next = new_node  # type: ignore
        self.length += 1
        return True


my_linked_list = LinkedList(0)
my_linked_list.append(2)

my_linked_list.insert(1, 1)

my_linked_list.print_list()
