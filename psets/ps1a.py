from calendar import month

annual_salary = float(input('What is your annual salary: '))

portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))

total_cost = float(input('What is the current cost of your dream home: '))

portion_down_payment = 0.25

current_savings = 0

r = 0.04 # ROI


month_count = 0

while current_savings <= total_cost*portion_down_payment:
    month_count+=1
    current_savings += (annual_salary/12)*(portion_saved)
    current_savings += current_savings*r/12


print('month_count:',month_count)
print('current_savings:',current_savings)

