table_count = int(input())
length_of_table = float(input())
width_of_table = float(input())

area_square = table_count * (length_of_table / 2) ** 2
area_rectangle = table_count * (length_of_table+2 * 0.30) * (width_of_table+2 * 0.30)
price_usd = area_square * 9.00+area_rectangle * 7.00
price_bgn = price_usd * 1.85


print(f'{price_usd:.2f} USD')
print(f'{price_bgn:.2f} BGN')
