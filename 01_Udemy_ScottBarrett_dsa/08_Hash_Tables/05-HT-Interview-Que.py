# this is a very common interview question, so you may see some version of this question later on.
# Question:
"""there are 2 lists. what we want to determine is whether these 2 lists have an item in common."""
# there will be 2 approaches for this, the second one is the more efficient one.

# approach 1: navive appraoch: which is to create a nested loop. -> O(n²)
""" def item_in_common(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False


list1 = [1, 3, 5]
list2 = [2, 4, 5]

print(item_in_common(list1, list2)) """

# approach 2: more efficient way. --> O(n)
# O(n) is far more efficient than O(n²).


def item_in_common(list1, list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True

    for j in list2:
        if j in my_dict:
            return True

    return False


list1 = [1, 3, 5]
list2 = [2, 4, 5]

print(item_in_common(list1, list2))


# NOTE: this here is not a nested loop. They are one after the other!
