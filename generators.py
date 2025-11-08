# Generators are functions that return an object that can be iterated over
# It basically generates ONE element at a time in a given sequence
def mygenerator():
    yield 1
    yield 2
    yield 3

g = mygenerator()

# Shows 1 2 3 
# for i in g:
#     print(i)

# Using next to stop at the first yield after printing
value = next(g)
print(value)

# this starts again and prints the second yield
value = next(g)
print(value)