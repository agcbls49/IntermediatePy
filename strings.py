# Strings: Ordered, Immutable, Text Representation
my_string = "Hello World"
print(my_string)

my_string = 'I\'m a programmer'
my_string = "I'm a programmer"
print(my_string)

# Don't create a new line
my_string = """Hello \
World
I'm a programmer
"""
print(my_string)

# Create a new line (remove the back slash)
my_string = """Hello 
World
I'm a programmer
"""
print(my_string)

# Get character from string using array 
my_string = "Hello World"
char = my_string[0]
print(char)

# Access substring using slicing
# Prints ello
my_string = "Hello World"
substring = my_string[1:5]
print(substring)

# Reverse the string
substring = my_string[::-1]
print(substring)

# Concatenate string
greeting = "Hello"
name = "Tom"
sentence = greeting + " " + name
print(sentence)

# Iterate over a string
greeting = "Hello"
for i in greeting:
    print(i)

# Check if character or substring is inside the string
if 'e' in greeting:
    print('yes')
else: 
    print('no')

# Remove White Space from string
my_string = '    Hello World    '
my_string = my_string.strip()
print(my_string)

# Convert all to uppercase and lowercase
my_string = my_string.upper()
print(my_string)

my_string = my_string.lower()
print(my_string)

# Check if string starts with specific character or substring
# This is case sensitive
my_string = "Hello World"
print(my_string.startswith('Hello'))

# Check if string ends with specific character or substring
print(my_string.endswith('d'))

# Find index of a character or substring
# returns -1 if string cannot be found
print(my_string.find('o'))

# Count the number of characters in the string
print(my_string.count('o'))

# Replace characters or substring in the string
print(my_string.replace('World', "Universe"))

# Convert string to a list and 
# put each word of the string as an element inside the list
my_string = 'how are you doing'

# default argument of the split is a space so it takes the words
# by checking if there is a space on the string
# A delimiter can be added like .split(",")
my_list = my_string.split()
print(my_list)

# Using the delimeter
my_string = 'how,are,you,doing'
my_list = my_string.split(",")
print(my_list)

# Convert list back to string
new_string = ' '.join(my_list)
print(new_string)

# Create 6 a's inside an array then 
# use join to connect all a's together as a string
my_list = ['a'] * 6
my_string = ''.join(my_list)
print(my_string)

# Formatting strings
# using % sign
var = "Tom"
my_string = "The variable is %s" % var
print(my_string)

# use %d for integer 
var = 3
my_string = "The variable is %d" % var
print(my_string)

# use %f for float
var = 3.1234567
# print up to two decimal places only
my_string = "The variable is %.2f" % var
print(my_string)

# using format
var = "Tom"
my_string = "The variable is {}".format(var)
print(my_string)

# using float in format
var = 3.1234567
var2 = 6
my_string = "The variable is {:.2f} and {}".format(var, var2)
print(my_string)

# using f strings (best way)
var = "Tom"
my_string = f"The variable is {var}"
print(my_string)