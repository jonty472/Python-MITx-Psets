annual_salary = 150000
#float(input('What is your annual salary: '))

portion_saved = 0
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

saving_rate = dp_monthly/monthly_salary

#print(saving_rate)


month_count = 0




x = 12500 #montly salary
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low)/2.0

while ans*36 != downpayment:
    #print('low =', low, 'high =', high, 'ans =', ans)
    numGuesses+=1

    if ans*36 < downpayment:
        low = ans
    else:
        high = ans
    ans = (high+low)/2.0


print(ans/monthly_salary)
print(numGuesses)

    
