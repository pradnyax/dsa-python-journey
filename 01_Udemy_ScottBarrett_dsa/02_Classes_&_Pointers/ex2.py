# Pointers

num1 = 11
num2 = num1

print("Before num2 value is updated: ")
print("num1 = ", num1)
print("num2 = ", num2)

print("\nnum1 points to: ", id(num1))
print("num2 points to: ", id(num2))

# in memory, num2 points to the same address as num1

print("------------------------------")
num2 = 22

print("After num2 value is updated: ")
print("num1 = ", num1)
print("num2 = ", num2)

print("\nnum1 points to: ", id(num1))
print("num2 points to: ", id(num2))

# in memory, it points to different adresses now.
# NOTE: INTEGERS are immutable.
