# Sets: Unordered, Mutable, No Duplicates
myset = {1, 2, 3}
print(myset)

# No duplicates so only 1, 2, 3 are printed
myset = {1, 2, 3, 1, 2}
print(myset)

# Use set function with iterable list
myset = set([1, 2, 3])
print(myset)

# Set with String
myset = set("Hello")
print(myset)

# Create an empty set
myset = set()
myset.add(1)
myset.add(2)
myset.add(3)
print(myset)

# Remove/Discard elements 
myset.remove(3)
myset.discard(3)
print(myset)

# Clear the list
myset.clear()
print(myset)

# Remove the curly and return 1 (LIFO - Last in First Out)
print(myset.pop())
# this shows 2 & 3
print(myset)

# Iterate through the set
for i in myset:
    print(i)

# Check if element is inside the set
if 1 in myset:
    print("yes")
else:
    print("no")

# Union
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

# Combine elements from two sets without duplicating
u = odds.union(evens)
print(u)

# Intersection
# Only take elements that are found in both sets / common elements only
# this shows 3, 5, 7
i = odds.intersection(primes)
print(i)

# Difference
# Returns all elements that are not in the first set
# Returns 4, 5, 6, 7, 8, 9 because it returns the elements from the first set 
# but not the elements from the second set as 1, 2, 3 are both in setA and setB
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
diff = setA.difference(setB)
print(diff)

# Symmetric Difference
# will return a set that contains elements from setA and setB but not in both sets
# This return 4, 5, 6, 7, 8, 9, 10, 11, 12 in both setA and setB
diff = setA.symmetric_difference(setB)
print(diff)

# Use Update to modify the sets
# updates the set by adding elements found in 
# another set so this prints 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
setA.update(setB)
print(setA)

# Intersection Update
# updates the set by keeping only the elements found in both sets so only 1, 2, 3 are returned
setA.intersection_update(setB)
print(setA)

# Difference Update
# updates the set by removing elements found in another set so only 4, 5, 6, 7, 8, 9 are returned
setA.difference_update(setB)
print(setA)

# Symmetric Difference Update
# updates the set by only keeps elements found in setA and setB but not elements found in both
# so it returns 4, 5, 6, 7, 8, 9, 10, 11, 12
setA.symmetric_difference_update(setB)
print(setA)

# Subset
setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
# This returns false because subset that all the elements in the first set are also in the second set
print(setA.issubset(setB))

# Superset - opposite of subset
# This returns false because a superset returns true if the first set
# contains all the numbers from the second set
print(setB.issuperset(setA))

# Disjoint Sets - Returns True if both sets have the same element
print(setA.isdisjoint(setB))

# Copying two sets using copy or set function
setB = setA.copy()
setB = set(setA)
print(setB)

# Frozen Set - just an immutable version of a normal set
a = frozenset([1, 2, 3, 4])
print(a)