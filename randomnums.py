import random

# Random float from 0 to 1
a = random.random()
print(a)

# Specify range of random using uniform
# this will show a random float
a = random.uniform(1, 10)
print(a)

# Use randint for getting a random integer
a = random.randint(1, 10)
print(a)

# Pick a random range but 10 is not included
a = random.randrange(1, 10)
print(a) 

# Random Normal used for statistics which 
# picks a mean of 0 and standard deviation of 1
a = random.normalvariate(0, 1)
print(a)

# Pick a random letter or element in the list
mylist = list('ABCDEFGH')
a = random.choice(mylist)
print(a)

# Pick 3 random elements but its unique (no duplicates)
mylist = list('ABCDEFGH')
a = random.sample(mylist, 3)
print(a)

# The same elements can be picked multiple times (allows duplicates)
mylist = list('ABCDEFGH')
a = random.choices(mylist, k=3)
print(a)

# Shuffle a list in place
mylist = list('ABCDEFGH')
random.shuffle(mylist)
print(mylist)