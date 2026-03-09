# pointers

dict1 = {"value": 11}

dict2 = dict1

print("Brfore value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to: ", id(dict1))
print("dict2 points to :", id(dict2))

# now, both dict will point to the same address in memory.
print("===============================")

dict2["value"] = 22

print("After value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to: ", id(dict1))
print("dict2 points to :", id(dict2))

# here, the value changes but the memory adress remains the same, ie, dict1=22, dict2=22

# NOTE: dictionaries are mutable.
