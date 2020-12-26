lilly_age = int(input())
price_wash_machine = float(input())
price_toy = int(input())

money = 10.0
savings = 0.0
brother = 1.0
toys = 0

for year in range(1, lilly_age+1):
    if year % 2 == 0:
        savings += money
        money += 10.0
        savings -= brother
    else:
        toys += 1

money_sold = toys * price_toy
savings += money_sold
money_left = abs(savings - price_wash_machine)
money_left = f'{money_left:.2f}'

if savings >= price_wash_machine:
    print(f'Yes! {money_left}')
else:
    print(f'No! {money_left}')
