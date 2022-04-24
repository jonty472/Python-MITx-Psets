annual_salary = float(input('What is your annual salary: '))

total_cost = 1000000


annual_raise = 0.07


portion_down_payment = 0.25

current_savings = 0

roi = 0.04 # Return on investment

downpayment = total_cost*portion_down_payment

x = 150000

tolerance = 100

high = max(1.0, x)

low = 0.0

numGuesses = 0

ans = (high + low)//2


while abs(current_savings - downpayment) >= tolerance:
    #print('low =', low, 'high =', high, 'ans =', ans)
    current_savings = 0

    # used in for loop
    for_annual_salary = annual_salary

    rate = ans/x

    for month in range(36):

        if month%6 == 0 and month > 0:
            for_annual_salary += for_annual_salary*annual_raise
            #print('annual raise applied:', annual_salary)
        
        monthly_salary = for_annual_salary/12

        # Calc current_savings
        current_savings += monthly_salary*rate + (current_savings*roi/12)



    if current_savings < downpayment:
        low = ans
    else:
        high = ans
    
    ans = (high + low)//2
    numGuesses+=1
    if numGuesses>13:
        break


print('Best savings rate: {:.4f}'.format(rate))
print('numGuesses in bisection search:', numGuesses)