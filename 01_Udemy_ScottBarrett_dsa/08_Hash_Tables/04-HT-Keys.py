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

    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):  # type: ignore
                    all_keys.append(self.data_map[i][j][0])  # type: ignore
        return all_keys


my_ht = HashTable()

my_ht.set_item("bolts", 1400)
my_ht.set_item("washers", 50)
my_ht.set_item("lumber", 70)

print(my_ht.keys())
