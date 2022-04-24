"""
Finger exercise: Write a function isIn that accepts two strings as arguments and
returns True if either string occurs anywhere in the other, and False otherwise.
Hint: you might want to use the built-in str operation in
"""

def isIn(x, y):
    if x in y or y in x:
        is_in = True
    else:
        is_in = False
    return print(is_in)


isIn('abcdef', 'def')

isIn('alex', 'jeff')