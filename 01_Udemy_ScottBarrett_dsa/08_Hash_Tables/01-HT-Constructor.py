"""HASH TABLE"""


class HashTable:
    def __init__(self, size=7):
        # this is going to create a list of 7 items in it, and all of those will contain None.
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)


my_ht = HashTable()

my_ht.print_table()


# NOTE: this list is called data_map

""" NOTE: you should always have a prime number of addressesin HashTable.
And the reason for that is a prime number increases the amount of randomness for how the key value pairs are going to be distributed through the hash table, so it reduces your collisions. """
# Remember, the hash is what we pass the key to, to determine the address where we store that key value pair.
""" Hash method: This is the "magic machine." It takes a string (the Key) and turns it into an index number between 0 and size - 1.

Note: In Python, we use an underscore _ before the name (like __hash) to signal that this is an internal method, it's meant to be used by the class itself, not called directly from the outside. """


# output:
""" 
0 :  None
1 :  None
2 :  None
3 :  None
4 :  None
5 :  None
6 :  None 
"""
