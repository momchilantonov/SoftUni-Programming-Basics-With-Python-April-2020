honey_for_winter = float(input())

total_extraction = 0

while True:
    name = input()
    if name == 'Winter has come':
        break

    for i in range(6):
        extraction = float(input())
        total_extraction += extraction
    if total_extraction < 0:
        print(f'{name} was banished for gluttony')
    if total_extraction >= honey_for_winter:
        break

if total_extraction >= honey_for_winter:
    honey_surplus = total_extraction-honey_for_winter
    print(f'Well done! Honey surplus {honey_surplus:.2f}.')
else:
    honey_needed = honey_for_winter-total_extraction
    print(f'Hard Winter! Honey needed {honey_needed:.2f}.')
