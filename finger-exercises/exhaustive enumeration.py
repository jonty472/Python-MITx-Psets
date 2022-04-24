"""
Finger exercise: Write a program that asks the user to enter an integer and
prints two integers, root and pwr , such that 0 < pwr < 6 and root**pwr is equal
to the integer entered by the user. If no such pair of integers exists, it should
print a message to that effect.
"""
x = int(input('Enter a Interger: '))

root = 1
pwr = 1
found = False

while root**pwr != abs(x):
    pwr+=1

    # maintaining conditions (0 < pwr < 6) 
    # creating a cycle for root every 6 pwr. root is +1 e.g. 1^6 carries over to 2^1
    if pwr > 6:
        pwr=1
        root+=1
    
    # print statement if root and pwr found for x
    elif root**pwr == abs(x):
        found=True
        print(x,'is equal to',root,'**',pwr)

    else:
        continue
        

if not found:
    print('no such pair of integers exists')