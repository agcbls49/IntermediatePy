# Tuple: Ordered, Immutable (Changing elements by assignment of index is not allowed) 
# and allows Duplicate Elements
# As long as there is a comma then it will be recogniozed as a tuple
# Parethesis on both sides can also be added for easy distinction
my_tuple = "Max", "28", "Boston"
print(my_tuple)

# Built in tuple function can also be used
my_tuple = tuple(["Max", "28", "Boston"])
print(my_tuple)

# Access elements inside a tuple
# First element
item = my_tuple[0]
print(item)

# Second last element
item = my_tuple[-2]
print(item)

# Last element
item = my_tuple[-1]
print(item)

# Print elements of the tuple
for i in my_tuple:
    print(i)

# Check if element is inside the tuple
if "Max" in my_tuple:
    print("yes")
else:
    print("no")

my_tuple = ['a', 'p', 'p', 'l', 'e']
# Get the number of elements in the tuple
print(len(my_tuple))

# Count elements or number of p inside the tuple
print(my_tuple.count('p'))

# Find the index of specific element
print(my_tuple.index('l'))

# Convert tuple to list
mylist = list(my_tuple)
print(mylist)

# Convert list to tupple
my_tuple = tuple(mylist)
print(my_tuple)

# Slicing tuples
a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# Prints index number 2 element all the way to 5 which shows (3, 4, 5)
b = a[2:5]
print(b)

# Using Step Index
b = a[::2]
print(b)

# Unpacking - assigning the individual elements of a tuple to separate variables
my_tuple = "Max", 28, "Boston"
name, age, city = my_tuple
print(name)
print(age)
print(city)

my_tuple = (0, 1, 2, 3, 4)
i1, *i2, i3 = my_tuple
print(i1)
# all elements in between first and last index converted into a list using an asterisk
print(i2)
print(i3)

# Working with tuples can be more efficient compared to lists
import sys
mylist = [0, 1, 2, "hello", True]
my_tuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(mylist), "bytes")
print(sys.getsizeof(my_tuple), "bytes")