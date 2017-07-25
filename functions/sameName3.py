# http://automatetheboringstuff.com/chapter3/
# In a function, a variable will either always be global or always be local. 

def spam():
    global eggs
    eggs = 'spam' # this is global

def bacon():
    eggs = 'bacon' # this is local

def ham():
    print(eggs) # this is the global

eggs = 42 # this is the global
spam()
print(eggs)
