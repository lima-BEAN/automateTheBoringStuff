# http://automatetheboringstuff.com/chapter3/
# the value that a function call evaluates to
# is called the return value of the function.

# you can specify what the return value should be with a return statement
# return statement consists of:
# The 'return' keyword and the value or expression that the function
# should return

import random
def getAnswer(ansNum):
    if ansNum == 1:
        return 'It is certain'
    elif ansNum == 2:
        return 'It is decidely so'
    elif ansNum == 3:
        return 'Yes'
    elif ansNum == 4:
        return 'Reply hazy try again'
    elif ansNum == 5:
        return 'Ask again later'
    elif ansNum == 6:
        return 'Concentrate and ask again'
    elif ansNum == 7:
        return 'My reply is no'
    elif ansNum == 8:
        return 'Outlook not so good'
    elif ansNum == 9:
       return 'Very doubtful'

r = random.randint(1,9)
fortune = getAnswer(r)
print(str(r) + ': ' + fortune)

# ^ can be compressed to:
# print(getAnswer(random.randint(1, 9)))
