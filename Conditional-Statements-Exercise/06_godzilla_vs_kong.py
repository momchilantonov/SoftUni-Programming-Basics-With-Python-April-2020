budget = float(input())
actors = int(input())
clothes_price = float(input())

decor = budget * 0.1

if actors > 150:
    clothes = clothes_price * actors * 0.9
else:
    clothes = clothes_price * actors

needed_money = decor + clothes
total_money = budget - needed_money
not_enough_money = abs(needed_money - budget)

if needed_money > budget:
    print('Not enough money!')
    print(f'Wingard needs {not_enough_money:.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {total_money:.2f} leva left.')
