bees_qty = int(input())
bear_hp = int(input())
bear_power = int(input())

bees_left = bees_qty

while bees_left >= 100:
    bees_left = bees_left-bear_power
    bear_hp = bear_hp-bees_left * 5
    if bear_hp <= 0:
        print(f'Beehive won! Bees left {bees_left}.')
        break

if bees_left <= 0:
    bees_left = 0
    print(f'The bear stole the honey! Bees left {bees_left}.')
elif bees_left < 100:
    print(f'The bear stole the honey! Bees left {bees_left}.')
