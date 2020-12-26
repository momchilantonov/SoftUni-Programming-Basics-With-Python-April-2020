import math

bees_qty = int(input())
flowers_qty = int(input())

total_honey_qty = bees_qty * flowers_qty * 0.21

honey_cakes_qty = math.floor(total_honey_qty / 100)

residual_honey_qty = total_honey_qty - honey_cakes_qty * 100

print(f"{honey_cakes_qty} honeycombs filled.")
print(f"{residual_honey_qty:.2f} grams of honey left")
