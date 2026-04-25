# set_item() --> The set item method is going to use the hash method on the key to create the address. And then it's also going to create a key value pair in a list.


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


my_ht = HashTable()

my_ht.set_item("bolts", 1400)
my_ht.set_item("nuts", 50)
my_ht.set_item("screws", 70)

my_ht.print_table()
