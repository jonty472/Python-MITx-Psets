"""
Newton-Raphson for sqaure root
Finding x such that x**2 - 24 is within epsilon of 0
"""

epsilon = 0.1
k = 24.0
numGuesses = 0

guess = k/2.0

while abs(guess*guess - k) >= epsilon:
    numGuesses+=1
    
    guess = guess - (((guess**2) - k)/(2*guess))
    print('Square root of', k, 'is about', guess)
    print('num of guesses: ',numGuesses)