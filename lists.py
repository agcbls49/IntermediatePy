# Lists: Ordered, Mutable, Allows Duplicate Elements
my_list = ["banana", "cherry", "apple"]
print(my_list)

# create an empty list to later append items onto
my_list2 = list()
print(my_list2)

# List with other data types
my_list2 = [5, True, "apple", "apple"]
print(my_list2)

# Access an element inside the array/list
item = my_list[0]
print(item)

# Get the last item of the list using -1
# Change to -2 to get the second last item from the list
item = my_list[-1]
print(item)

# Iterate through the list and print all elements inside
for i in my_list:
    print(i)

# Check if item is inside the list
if "banana" in my_list:
    print("yes")
else:
    print("no")

# Check how many elements inside the list
print(len(my_list))

# Append items to the list
my_list.append("lemon")
print(my_list)

# Insert item at a specific position
my_list.insert(1, "blueberry")
print(my_list)

# Remove items inside the list
# Returns the last item and also removes it
item = my_list.pop()
print(item)
print(my_list)

# Remove a specific element
item = my_list.remove("cherry")
print(my_list) 

# Remove all elements using Clear
item = my_list.clear()
print(my_list)

# Reverse the list
item = my_list.reverse()
print(my_list)

# Sort the list
item = my_list.sort()
print(my_list)

# Sort list of numbers
my_list = [4, 3, 1, -1, -5, 10]
item = my_list.sort()
print(my_list)

# Create list with 5 zeros
my_list = [0] * 5
print(my_list)

# Add two lists together
my_list = [0] * 5
my_list2 = [1, 2, 3, 4, 5]
new_list = my_list + my_list2
print(new_list)

# Slicing - access some parts of the list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# specify start and stop index which in this case is 1 and 5
# the last index is excluded so the list is [2, 3, 4, 5]
a = my_list[1:5]
# if no start index is specified then it starts from the beginning
# if no stop index is specified then it goes all the way to the end
print(a)

# Slicing with Step index (optional)
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Default Step index is 1
# This goes all the way from the beginning to the end with a step index of 1
a = my_list[::1]

# If step index is 2 then it takes every second item
a = my_list[::2]

# A negative index just reverses the list
a = my_list[::-1]
print(a)

# Copying a list
list_orig = ["banana", "cherry", "apple"]
# Copies the contents of the original list and allows modification without changing the original list
list_copy = list_orig.copy()
list_copy.append("lemon")

# Another way to do this is instead of copy just use list(original_list)
list_copy = list(list_orig)
list_copy.append("lemon")

# Slicing can also be used to create a copy of the original list
list_copy = list_orig[:]
list_copy.append("lemon")

# list_copy shows the lemon but the original list stays the same
print(list_copy)
print(list_orig)

# List Comprehension
# Create new list from an existing list all in one line
my_list = [1, 2, 3, 4, 5, 6]
# create list of squared numbers
b = [i*i for i in my_list]
print(my_list)
# This shows the newly created list of squared numbers based off of my_list
print(b)