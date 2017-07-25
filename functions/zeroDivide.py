# Error handling
# http://automatetheboringstuff.com/chapter3/
# Errors can be handled with try and except statements
# The code that could potentially have an error is put in a try clause.

# The program execution moves to the start of a following except clause if
# an error happens.


def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')
        
print(spam(2))
print(spam(12))
print(spam(0)) # will throw a divide-by-zero error
print(spam(1))
