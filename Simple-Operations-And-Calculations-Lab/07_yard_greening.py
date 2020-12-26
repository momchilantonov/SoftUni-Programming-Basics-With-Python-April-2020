qty_sq_m = float(input())

price_for_sq_m = 7.61
discount = 0.82

total_price_without_discount = qty_sq_m * price_for_sq_m
discount_in_lv = total_price_without_discount-(total_price_without_discount * discount)
total_price_with_discount = total_price_without_discount-discount_in_lv

print(f'The final price is: {total_price_with_discount:.2f} lv.')
print(f'The discount is: {discount_in_lv:.2f} lv.')
