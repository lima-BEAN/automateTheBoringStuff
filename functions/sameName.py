# http://automatetheboringstuff.com/chapter3/
# Avoid using local variables that have the same name as
# a global variable or another local variable.

def spam():
    eggs = 'spam local'
    print(eggs) # prints 'spam local'

def bacon():
    eggs = 'bacon local' 
    print(eggs) # prints 'bacon local'
    spam()
    print(eggs) # prints 'bacon local'

eggs = 'global'
bacon()
print(eggs) # prints 'global'
