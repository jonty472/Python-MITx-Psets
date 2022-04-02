annual_salary = 150000
#float(input('What is your annual salary: '))

total_cost = 1000000
#float(input('What is the current cost of your dream home: '))

annual_raise = 0.07
#float(input('Enter the semi­annual raise, as a decimal:'))

portion_down_payment = 0.25

current_savings = 0

r = 0.04 # ROI

month_count = 0

numGuesses = 0

"""
 Python 3, if we want to use integer division instead of the standard float division, we can use the // operator:

"""
downpayment = total_cost*portion_down_payment

x = 250000

high = max(1.0, x)

low = 0.0

ans = (high + low)//2

#Accepts downpayment within + or - 100
while ans*36<=(downpayment - 100) or ans*36>=(downpayment+100):
    print('low =', low, 'high =', high, 'ans =', ans)
    numGuesses+=1

    if ans*36 < downpayment:
        low = ans
    else:
        high = ans
    
    ans = (high + low)//2

print(numGuesses)


while month_count != 36 and current_savings <= downpayment:
    month_count+=1

    if month_count%6 ==0:
        annual_salary += annual_salary*annual_raise
        #print('annual raise applied:', annual_salary)

    savings_rate = ans/(annual_salary/12)
    #print("{:.4f}".format(savings_rate))

    
    current_savings += savings_rate*(annual_salary/12)
    print('current savings:',current_savings,'at month count:',month_count)

    # ROI
    current_savings += current_savings*r/12
    


#print('current savings:',current_savings)
#print('month count:',month_count)

