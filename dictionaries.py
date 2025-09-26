# Dictionary: Key-Value Pairs, Unordered, Mutable (changeable)
my_dict = {"name": "Max", "age": 28, "city": "New York"}
print(my_dict)

# Create dictionary using the dict function
my_dict2 = dict(name="Mary", age=27, city="Boston")
print(my_dict2)

# Raise an exception because last name does'nt exist
try:
    print(my_dict["lastname"])
except:
    print("Error")

# Using a for loop
# Loop through all the keys
for key in my_dict:
    print(key)

# Loop through all the values
for values in my_dict.values():
    print(values)

# Print both key and values using for loop
for key, value in my_dict.items():
    print(key, value)

# Copy a dictionary
mydict_copy = my_dict.copy()
# the dic function can also be used to copy 
mydict_copy = dict(my_dict)
mydict_copy["email"] = "max@xyz.com"
print(mydict_copy)
print(my_dict)

# Merge two dictionaries using update
mydict = {"name": "Max", "age": 28, "email": "max@xyz.com"}
mydict2 = dict(name="Mary", age=27, city="Boston")
mydict.update(mydict2)
print(mydict)

# Possible key types
# to access the elements use the actual key number and not the index like a list
mydict = {3: 9, 6: 36, 9: 81}
print(mydict)

# Lists cannot be used as it is mutable but tuples can
mytuple = (8, 7)
mydict = {mytuple: 15}
print(mydict)