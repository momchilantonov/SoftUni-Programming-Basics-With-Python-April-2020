whiskey_price = float(input())
beer_liters = float(input())
wine_liters = float(input())
brandy_liters = float(input())
whiskey_liters = float(input())

brandy_price = whiskey_price / 2
wine_price = brandy_price - brandy_price * 0.4
beer_price = brandy_price - brandy_price * 0.8

sum_beer = beer_price * beer_liters
sum_wine = wine_price * wine_liters
sum_brandy = brandy_price * brandy_liters
sum_whiskey = whiskey_price * whiskey_liters

needed_money = sum_beer + sum_wine + sum_brandy + sum_whiskey

print(f'{needed_money:.2f}')
