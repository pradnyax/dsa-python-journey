# insert(index, value) ==> Creates a new node and squeezes it in at a specific spot/index.


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

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head  # type: ignore
            self.head.prev = new_node  # type: ignore
            self.head = new_node
        self.length += 1
        return True

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

    def insert(self, index, value):
        # case1: if index is out of range
        if index < 0 or index > self.length:
            return False

        # case2: insert new node at index:0
        if index == 0:
            return self.prepend(value)

        # case3: insert new node at end of DLL
        if index == self.length:
            return self.append(value)

        # case4: insert new node anywhere in the middle of DLL
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next  # type: ignore

        new_node.prev = before  # type: ignore
        new_node.next = after
        before.next = new_node  # type: ignore
        after.prev = new_node  # type: ignore

        self.length += 1
        return True


my_dll = DoublyLinkedList(1)
my_dll.append(3)

my_dll.insert(1, 11)

my_dll.print_list()
