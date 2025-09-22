# Tuple: Ordered, Immutable (Changing elements by assignment of index is not allowed) 
# and allows Duplicate Elements
# As long as there is a comma then it will be recogniozed as a tuple
# Parethesis on both sides can also be added for easy distinction
mytuple = "Max", "28", "Boston"
print(mytuple)

# Built in tuple function can also be used
mytuple = tuple(["Max", "28", "Boston"])
print(mytuple)

# Access elements inside a tuple
# First element
item = mytuple[0]
print(item)

# Second last element
item = mytuple[-2]
print(item)

# Last element
item = mytuple[-1]
print(item)

# Print elements of the tuple
for i in mytuple:
    print(i)

# Check if element is inside the tuple
if "Max" in mytuple:
    print("yes")
else:
    print("no")

mytuple = ['a', 'p', 'p', 'l', 'e']
# Get the number of elements in the tuple
print(len(mytuple))

# Count elements or number of p inside the tuple
print(mytuple.count('p'))

# Find the index of specific element
print(mytuple.index('l'))

# Convert tuple to list
mylist = list(mytuple)
print(mylist)

# Convert list to tupple
mytuple = tuple(mylist)
print(mytuple)

# Slicing tuples
a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# Prints index number 2 element all the way to 5 which shows (3, 4, 5)
b = a[2:5]
print(b)

# Using Step Index
b = a[::2]
print(b)

# Unpacking - assigning the individual elements of a tuple to separate variables
mytuple = "Max", 28, "Boston"
name, age, city = mytuple
print(name)
print(age)
print(city)

mytuple = (0, 1, 2, 3, 4)
i1, *i2, i3 = mytuple
print(i1)
# all elements in between first and last index converted into a list using an asterisk
print(i2)
print(i3)

# Working with tuples can be more efficient compared to lists
import sys
mylist = [0, 1, 2, "hello", True]
mytuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(mylist), "bytes")
print(sys.getsizeof(mytuple), "bytes")