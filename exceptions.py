# Errors and Exceptions
try:
    a = 5 / 0
except Exception as e:
    print(e)

# More specific errors
try:
    a = 5 / 1
    b = a + '10'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)