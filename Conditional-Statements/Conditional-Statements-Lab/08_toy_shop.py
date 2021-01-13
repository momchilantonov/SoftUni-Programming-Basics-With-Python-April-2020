# inputs
price_of_excursion = float(input())
qty_puzzles = int(input())
qty_dolls = int(input())
qty_teddy_bears = int(input())
qty_minions = int(input())
qty_trucks = int(input())

# constants (can be inputs)
price_puzzle = 2.60
price_dolls = 3.00
price_teddy_bear = 4.10
price_minion = 8.20
price_truck = 2.00

# rent and discount index
discount_index = 0.75
rent_index = 0.90

# orders qty and sum for each product
orders_qty = qty_puzzles + qty_dolls + qty_teddy_bears + qty_minions + qty_trucks
sum_puzzles = qty_puzzles * price_puzzle
sum_dolls = qty_dolls * price_dolls
sum_teddy_bears = qty_teddy_bears * price_teddy_bear
sum_minions = qty_minions * price_minion
sum_trucks = qty_trucks * price_truck

# calculate profit
profit = 0.00

if orders_qty >= 50:
    profit = ((sum_puzzles + sum_dolls + sum_teddy_bears + sum_minions + sum_trucks) * discount_index * rent_index)
else:
    profit = ((sum_puzzles + sum_dolls + sum_teddy_bears + sum_minions + sum_trucks) * rent_index)

# calculate rest and lack from the profit and print
rest_of_profit = 0.00
lack_for_excursion = 0.00

if profit >= price_of_excursion:
    rest_of_profit = profit - price_of_excursion
    print(f'Yes! {rest_of_profit:.2f} lv left.')
else:
    lack_for_excursion = price_of_excursion - profit
    print(f'Not enough money! {lack_for_excursion:.2f} lv needed.')
    