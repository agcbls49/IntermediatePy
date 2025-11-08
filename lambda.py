# lambda arguments: expression
# creates a function with some arguments 
# and evaluates the expression and returns a result

# Creates a function with one argument which is x
# and 10 gets added to x and returns its result
add10 = lambda x: x + 10
# Shows 15
print(add10(5))

mult = lambda x,y: x*y
# Shows 25
print(mult(5, 5))

points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
print(points2D)

# Sort list according to the y index
points2D_sorted = sorted(points2D, key=lambda x: x[1])
print(points2D_sorted)