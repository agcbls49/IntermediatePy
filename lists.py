# mylist = ["banana", "cherry", "apple"]
# print(mylist)

# create an empty list to later append items onto
# mylist2 = list()
# print(mylist2)

# List with other data types
# mylist2 = [5, True, "apple", "apple"]
# print(mylist2)

# Access an element inside the array/list
# item = mylist[0]
# print(item)

# Get the last item of the list using -1
# Change to -2 to get the second last item from the list
# item = mylist[-1]
# print(item)

# Iterate through the list and print all elements inside
# for i in mylist:
#     print(i)

# Check if item is inside the list
# if "banana" in mylist:
#     print("yes")
# else:
#     print("no")

# Check how many elements inside the list
# print(len(mylist))

# Append items to the list
# mylist.append("lemon")
# print(mylist)

# Insert item at a specific position
# mylist.insert(1, "blueberry")
# print(mylist)

# Remove items inside the list
# Returns the last item and also removes it
# item = mylist.pop()
# print(item)
# print(mylist)

# Remove a specific element
# item = mylist.remove("cherry")
# print(mylist) 

# Remove all elements using Clear
# item = mylist.clear()
# print(mylist)

# Reverse the list
# item = mylist.reverse()
# print(mylist)

# Sort the list
# item = mylist.sort()
# print(mylist)

# Sort list of numbers
# mylist = [4, 3, 1, -1, -5, 10]
# item = mylist.sort()
# print(mylist)

# Create list with 5 zeros
# mylist = [0] * 5
# print(mylist)

# Add two lists together
# mylist = [0] * 5
# mylist2 = [1, 2, 3, 4, 5]
# new_list = mylist + mylist2
# print(new_list)

# Slicing - access some parts of the list
# mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# specify start and stop index which in this case is 1 and 5
# the last index is excluded so the list is [2, 3, 4, 5]
# a = mylist[1:5]
# if no start index is specified then it starts from the beginning
# if no stop index is specified then it goes all the way to the end
# print(a)

# Slicing with Step index (optional)
# mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Default Step index is 1
# This goes all the way from the beginning to the end with a step index of 1
# a = mylist[::1]

# If step index is 2 then it takes every second item
# a = mylist[::2]

# A negative index just reverses the list
# a = mylist[::-1]
# print(a)

# Copying a list
list_orig = ["banan", "cherry", "apple"]
# Copies the contents of the original list and allows modification without changing the original list
# list_copy = list_orig.copy()
# list_copy.append("lemon")

# Another way to do this is instead of copy just use list(original_list)
# list_copy = list(list_orig)
# list_copy.append("lemon")

# Slicing can also be used to create a copy of the original list
# list_copy = list_orig[:]
# list_copy.append("lemon")

# list_copy shows the lemon but the original list stays the same
# print(list_copy)
# print(list_orig)

# List Comprehension
# Create new list from an existing list all in one line
mylist = [1, 2, 3, 4, 5, 6]
# create list of squared numbers
b = [i*i for i in mylist]
print(mylist)
# This shows the newly created list of squared numbers based off of mylist
print(b)