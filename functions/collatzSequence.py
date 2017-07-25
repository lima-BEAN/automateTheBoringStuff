# Practice problem
# http://automatetheboringstuff.com/chapter3/

# If number is even, print number // 2
# if odd, print 3 * number + 1

# Let user type in an integer and keeps calling collatz() on that
# number until the function returns the value 1

def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

print('Enter a number to see the collatz sequence.')
num = int(input())

collatzNum = collatz(num)
print(collatzNum)

while collatzNum != 1:
    collatzNum = collatz(collatzNum)
    print(collatzNum)


