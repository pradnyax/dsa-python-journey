# pop first ==> Removes the first node and returns it.
# Time complexity ==> O(1)


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

    def pop_first(self):
        # edge case1: there are zero/no items in the DLL
        if self.length == 0:
            return None

        temp = self.head
        # edge case2: there is only 1 item in the DLL
        if self.length == 1:
            self.head = None
            self.tail = None
        # edge case3: there are 2 or more items in DLL
        else:
            self.head = self.head.next  # type: ignore
            self.head.prev = None  # type: ignore
            temp.next = None  # type: ignore
        self.length -= 1
        return temp


my_dll = DoublyLinkedList(2)
my_dll.append(1)

print(my_dll.pop_first())  # (2) items in DLL - Returns 2 node
print(my_dll.pop_first())  # (1) item in DLL - Returns 1 node
print(my_dll.pop_first())  # (0) item in DLL - Returns None

# my_dll.print_list()
