# remove ==> remove a node/item at a particular index


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

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head  # type: ignore
            self.head = new_node
        self.length += 1
        return True  # NOTE: return True is optional here.

    def pop_first(self):
        if self.length == 0:
            return None

        temp = self.head
        self.head = self.head.next  # type: ignore
        temp.next = None  # type: ignore
        self.length -= 1

        if self.length == 0:
            self.tail = None
        return temp  # item that we removed from the LL

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next  # type: ignore
        return temp

    def remove(self, index):
        # case1: index is out of range in LL
        if index < 0 or index >= self.length:
            return None

        # case2: remove node from the beginning/head of LL
        if index == 0:
            return self.pop_first()

        # case3: remove node at the end of LL
        if index == self.length - 1:
            return self.pop()

        # case4: remove node from the middle of LL
        prev = self.get(index - 1)
        temp = prev.next  # type: ignore
        prev.next = temp.next  # type: ignore
        temp.next = None  # type: ignore
        self.length -= 1
        return temp
        # return temp.value     # only doing temp.value to get the node in the output, to test the code!


my_linked_list = LinkedList(11)

my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)

# my_linked_list.remove(2)
print(my_linked_list.remove(2), "\n")  # this will print out the node too.


my_linked_list.print_list()
