annual_salary = 150000
#float(input('What is your annual salary: '))

#portion_saved = 0
#float(input('Enter the percent of your salary to save, as a decimal: '))

total_cost = 1000000
#float(input('What is the current cost of your dream home: '))

annual_raise = .07
#float(input('Enter the semi­annual raise, as a decimal:'))

portion_down_payment = 0.25

current_savings = 0

r = 0.04 # ROI

downpayment = 250000

dp_monthly = downpayment/36

monthly_salary = 12500


month_count = 0

"""
write a program to calculate the best savings rate, as a function of your starting salary.

How much should you save each month to achieve this?

Tip - You can change the value being assesed in a while loop from inside (e.g. our salary changes every 6 months
so we need to take this into account)
Plan -

monthly_pay = annual_pay/12

low = 0.0
high = max(0.0, monthly pay)

#remeber values only being directly assesd can be changed
savings_rate = (high + low)/2.0

while savings <= downpayment:
    numGuess+=1
    month_count+=1

    if ans*36 < downpayment:
        low = high
    else:
        high = ans

    if month_count%6 == 0:
        apply_raise
        re-evulate monthly pay so ans takes in new variable
    
    current_saings = current_savings += (annual_salary/12)*(portion_saved)
"""

x = monthly_salary
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low)/2.0

saving_rate = dp_monthly/monthly_salary

# Calculates the monthly deposit need for 36 months
while current_savings<=downpayment:
    print('low =', low, 'high =', high, 'ans =', ans)
    numGuesses+=1
    month_count+=1

    if month_count%6 == 0:
        annual_salary += annual_salary*annual_raise
        monthly_salary = annual_salary/12
        ans = (max(1.0,(monthly_salary)) + low)/2.0
        print('raise applied: ', annual_salary)

    current_savings += (monthly_salary)*(saving_rate)
    #current_savings += current_savings*r/12

    if ans*36 < downpayment:
        low = ans
    else:
        high = ans
    ans = (high+low)/2.0


print(ans/monthly_salary)
print(numGuesses)
print('current savings:',current_savings)
    
