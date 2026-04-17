# delete first node from head side OR delete head = pop first


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
        # edge case1: LL is empty OR no/zero items in the LL
        if self.length == 0:
            return None
        # edge case2(a): LL has 2 or more items
        temp = self.head
        self.head = self.head.next  # type: ignore
        temp.next = None  # type: ignore
        self.length -= 1
        # edge case2(b) continued : for only 1 node/item in LL., (this will work after decremented by 1)
        if self.length == 0:
            self.tail = None
        return temp  # item that we removed from the LL
        # return temp.value


my_linked_list = LinkedList(2)
my_linked_list.append(1)


# (2) items - Returns 2 node
print(my_linked_list.pop_first())
# (1) item - Returns 1 node
print(my_linked_list.pop_first())
# (0) items - Returns None
print(my_linked_list.pop_first())


"""
output: 
<__main__.Node object at 0x0000027896666BA0>
<__main__.Node object at 0x0000027896914B90>
None
"""

# NOTE: if we do [return temp.value] on line 79, just for understanding logic purpose, we can see the output like below.
"""
output: 
2
1
None
"""
