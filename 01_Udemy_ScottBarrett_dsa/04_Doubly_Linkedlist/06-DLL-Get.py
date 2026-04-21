# get(index) ==> this is a index-based method.
#            ==> Finds and returns the node at a specific position/index.


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

    def get(self, index):
        # edge case1: index is out of range
        if index < 0 or index >= self.length:
            return None

        # edge case2: if the item is in the first half of the DLL
        temp = self.head
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next

        # edge case3: if item is in the second half of the DLL
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp


my_dll = DoublyLinkedList(1)

my_dll.append(2)
my_dll.append(3)
my_dll.append(4)

print(my_dll.get(1))  # get the item at the index 1
print(my_dll.get(2))  # get item at the index 2

# my_dll.print_list()

# NOTE: return temp.value ==> to get the output in terminal for better understanding.
