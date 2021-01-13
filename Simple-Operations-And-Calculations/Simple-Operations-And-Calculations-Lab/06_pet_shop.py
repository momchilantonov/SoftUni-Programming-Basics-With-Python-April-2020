qty_dogs = int(input())
qty_animals = int(input())

needed_money_for_dogs_food = float(qty_dogs * 2.50)
needed_money_for_animals_food = float(qty_animals * 4.0)
all_needed_money = needed_money_for_dogs_food + needed_money_for_animals_food

print(f'{all_needed_money:.2f} lv.')
