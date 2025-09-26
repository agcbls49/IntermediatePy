from timeit import default_timer as timer
my_list = ['a'] * 1000000

# bad
start = timer()
my_string = ''
for i in my_list:
    my_string += i
stop = timer()
# print time of the bad code
print(stop-start)

# good
start = timer()
my_string = ''.join(my_list)
stop = timer()
print(stop-start)