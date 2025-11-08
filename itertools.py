# itertools: product, permutations, combinations, accumulate, 
# groupby, and infinite iterators

# Import Product
print("Product")
from itertools import product
a = [1, 2]
b = [3, 4]
prod = product(a, b)

# Compute the Cartesion Product of the iterables
# Shows [(1, 3), (1, 4), (2, 3), (2, 4)]
print(list(prod))

# Define number of repetitions which makes a large list
a = [1, 2]
b = [3]
prod = product(a, b, repeat=2)
print(list(prod))

# Import Permutations
print("\nPermutations")
from itertools import permutations
a = [1, 2, 3]
perm = permutations(a)
# Print all possible orders of the list
print(list(perm))

# Specify the number of permutations
perm = permutations(a, 2)
print(list(perm))

# Combinations
print("\nCombinations")
from itertools import combinations, combinations_with_replacement
a = [1, 2, 3, 4]
# Must add length
comb = combinations(a, 2)
print(list(comb))

# Combinations with Replacement
print("\nCombinations with Replacement")
comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))

# Accumulate returns accumulated sums or binary functions
print("\nAccumulate")
from itertools import accumulate
a = [1, 2, 3, 4]
print("\nNormal List")
print(a)

# Basically 1, 3 (1 + 2), 6 (3 + 3), 10 (6 + 4)
print("\nAccumulated List")
acc = accumulate(a)
print(list(acc))

# Multiply the elements
print("\nAccumulate by Multiplying")
import operator
# Basically 1, 2 (1*2), 6 (3*2), 24 (6*4)
acc = accumulate(a, func=operator.mul)
print(list(acc))

# Accumulate with the Maximum Value
a = [1, 2, 5, 3, 4]
print("\nAccumulate with Max")
# Basically 1, 2, 5 (sees max value in the middle), 5, 5
acc = accumulate(a, func=max)
print(list(acc))

# Group By returns keys and groups from an iterable
print("\nGroup By")
from itertools import groupby

def smaller_than_3(x):
    # returns a boolean
    return x < 3

a = [1, 2, 3, 4]
group_obj = groupby(a, key=smaller_than_3)

# Shows True [1, 2] & False [3, 4]
for key, value in group_obj:
    print(key, list(value))