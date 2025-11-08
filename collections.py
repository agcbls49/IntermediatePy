#  Collections: Counter, namedtuple, OrderedDict, defaultdict, deque

# Use Counter count hashable objects
from collections import Counter
a = "aaaaabbbbccc"
my_counter = Counter(a)
# Shows the count of a, b, c
print(my_counter)

# Items Prints all the key values pairs
print(my_counter.items())

# Keys prints the keys so a, b, c
print(my_counter.keys())

# Values shows the counts 5, 4, 3
print(my_counter.values())

# Print the most common element with tuple
# returns a list with tuples in it
# Shows [('a', 5)]
print(my_counter.most_common(1))

# Print the two most common elements
# Shows [('a', 5), ('b', 4)]
print(my_counter.most_common(2))

# Print only the most common element without tuple
# Shows ('a', 5)
print(my_counter.most_common(1)[0])

# Elements returns an iterator over elements repeating each as 
# many times as its count but needs to be a list() first
print(list(my_counter.elements()))

# Named Tuple is similar to a struct
from collections import namedtuple
# class name is the string Point similar to the variable name
# this creates a classs called Point with fields x and y
Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
# Shows Point(x=1, y=-4)
print(pt)

# Access the field / print the values of x and y
# Shows 1 -4
print(pt.x, pt.y)

# Ordered Dictionary is like a regular dictionary but they 
# remember the order that the items were inserted
# kind of unnecessary since its guranteed in newer Python versions
from collections import OrderedDict
ordered_dict = OrderedDict()

ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['a'] = 1
# Shows OrderedDict({'b': 2, 'c': 3, 'd': 4, 'a': 1})
print(ordered_dict)

# DefaultDict is similar to the default but it has a default value 
# if the key has not been set yet
from collections import defaultdict

# Create a dictionary with a default value of integers
d = defaultdict(int)

d['a'] = 1
d['b'] = 2
# Shows defaultdict(<class 'int'>, {'a': 1, 'b': 2})
print(d)

# Access the keys
# Shows 1
print(d['a'])

# If an element that doesnt exist is accessed 
# then it will return a default value of 
# 0 (int), 0.0 (float), [] (list)
print(d['c'])

# Deque is a double ended queue and can be 
# used to add or remove elements from both ends  
from collections import deque
d = deque()
d.append(1)
d.append(2)
d.appendleft(3)
# Shows deque([3, 1, 2])
print(d)

# Remove the last element
d.pop()
print(d)

# Remove the element from the left
d.popleft()
print(d)

# Remove all the elements
d.clear()
print(d)

# Add multiple elements in one line
d.extend(([1, 2]))
d.extend(([4, 5, 6]))
# Shows deque([1, 2, 4, 5, 6])
print(d)

# Add multiple elements on the Left Side in one line
d.extendleft(([7, 8, 9]))
# Shows deque([9, 8, 7, 4, 5, 6])
print(d)

# Rotate all elements one place to the right
d.rotate(1)
print(d)

# Rotate to the left side 
d.rotate(-2)
print(d)