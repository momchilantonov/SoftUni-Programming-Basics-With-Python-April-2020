degrees = int(input())  # градусите за частта на деня
part_of_the_day = input()  # част на деня

outfit = ''  # облекло!!!
shoes = ''  # обувки!!!

if part_of_the_day == 'Morning' and 10 <= degrees <= 18:  # проверка кога трябва да се носи Sweatshirt и Sneakers
    outfit = 'Sweatshirt'
    shoes = 'Sneakers'
elif part_of_the_day == 'Afternoon' and degrees >= 25:  # проверка кога трябва да се носи Swim Suit и Barefoot
    outfit = 'Swim Suit'
    shoes = 'Barefoot'
elif (part_of_the_day == 'Afternoon' and 18 < degrees <= 24) \
        or (part_of_the_day == 'Morning' and degrees >= 25):  # проверка кога трябва да се носи T-Shirt и Sandals
    outfit = 'T-Shirt'
    shoes = 'Sandals'
elif part_of_the_day == 'Evening' or (part_of_the_day == 'Afternoon' and 10 <= degrees <= 18) \
        or (part_of_the_day == 'Morning' and 18 < degrees <= 24):  # проверка кога трябва да се носи Shirt и Moccasins
    outfit = 'Shirt'
    shoes = 'Moccasins'

print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")  # принтираме
