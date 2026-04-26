class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []  # type: ignore
        self.data_map[index].append([key, value])  # type: ignore

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):  # type: ignore
                if self.data_map[index][i][0] == key:  # type: ignore
                    return self.data_map[index][i][1]  # type: ignore
        return None


my_ht = HashTable()

my_ht.set_item("bolts", 1400)
my_ht.set_item("washers", 50)

print(my_ht.get_item("bolts"))
print(my_ht.get_item("washers"))
print(my_ht.get_item("lumber"))


""" 
NOTE: The get_item method is where you see the O(1) speed of a Hash Table in action. 
Instead of searching through every single cubby, you use the key to "teleport" exactly to the right address.
However, because we used Separate Chaining (putting lists inside our cubbies to handle collisions), there is one tiny extra step: once we get to the right cubby, we have to look through the small list inside it to find our specific key. 
"""
