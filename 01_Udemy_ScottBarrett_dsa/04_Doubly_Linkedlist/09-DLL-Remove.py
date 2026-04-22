# remove(index) ==>  Pulls out a node from a specific spot/index in DLL.


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

    def pop_first(self):
        if self.length == 0:
            return None

        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next  # type: ignore
            self.head.prev = None  # type: ignore
            temp.next = None  # type: ignore
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        temp = self.head
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next  # type: ignore

        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev  # type: ignore
        return temp

    def remove(self, index):

        # edge case1: index is out of range
        if index < 0 or index >= self.length:
            return None

        # case2: to remove the first item/node
        if index == 0:
            return self.pop_first()

        # case3: to remove the last item/node
        if index == self.length - 1:
            return self.pop()

        # case4: remove an item/node from the middle of DLL
        temp = self.get(index)

        temp.next.prev = temp.prev  # type: ignore
        temp.prev.next = temp.next  # type: ignore
        temp.next = None  # type: ignore
        temp.prev = None  # type: ignore
        self.length -= 1
        return temp


my_dll = DoublyLinkedList(0)
my_dll.append(1)
my_dll.append(2)

# my_dll.remove(1)
print(my_dll.remove(1), "\n")

my_dll.print_list()


# NOTE: in case4: we can code this with a different way using a before and after of temp too!
