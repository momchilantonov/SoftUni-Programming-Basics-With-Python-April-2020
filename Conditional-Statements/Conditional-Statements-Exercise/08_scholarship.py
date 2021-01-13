import math

incomes = float(input())
average_success = float(input())
minimum_wage = float(input())

social_scholarship = 0
scholarship_for_excellence = 0

if incomes < minimum_wage and average_success > 4.5:
    social_scholarship = minimum_wage * 0.35

if average_success >= 5.5:
    scholarship_for_excellence = average_success * 25

if social_scholarship > scholarship_for_excellence:
    print(f'You get a Social scholarship {math.floor(social_scholarship)} BGN')
elif scholarship_for_excellence > social_scholarship:
    print(f'You get a scholarship for excellent results {math.floor(scholarship_for_excellence)} BGN')
else:
    print('You cannot get a scholarship!')
