campaign_days = int(input())
pastry_cooks = int(input())
qty_cakes = int(input())
qty_waffles = int(input())
qty_pancakes = int(input())

products_costs = 8
cake_price = 45.00
waffle_price = 5.80
pancake_price = 3.20

price_cakes_per_day = qty_cakes * cake_price
price_waffles_per_day = qty_waffles * waffle_price
price_pancakes_per_day = qty_pancakes * pancake_price
sum_products_per_day = (price_cakes_per_day + price_waffles_per_day + price_pancakes_per_day) * pastry_cooks
sum_products_campaign = sum_products_per_day * campaign_days
sum_products_campaign_without_cots = sum_products_campaign - sum_products_campaign / products_costs

print(f'{sum_products_campaign_without_cots:.2f}')
