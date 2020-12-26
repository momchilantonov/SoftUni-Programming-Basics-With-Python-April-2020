budget = int(input())  # бюджет за риболов
season = input()  # сезон през който ще се наема кораба - "Spring"-3000, ("Summer", "Autumn"-4200), "Winter"-2600;
fishers_count = int(input())  # брой на рибарите <=6 (10%), 7<= брой на рибарите >=11 (15%), брой на рибарите >12 (25%)
# ако рибарите са четен брой и не е есен има допълнителна отстъпка от 5%

amount = 0  # първоначална сума !!!

if season == 'Spring':  # проврка през пролетта
    amount = 3000  # цена 3000лв
    if fishers_count <= 6:  # проврка до 6 рибаря
        amount = amount * 0.9  # сума с 10% отстъпка
    elif 7 <= fishers_count <= 11:  # проверка между 7 и 11 рибаря
        amount = amount * 0.85  # сума с 15% отстъпка
    elif fishers_count > 12:  # проврка над 12 рибаря
        amount = amount * 0.75  # сума с 25% отстъпка
elif season == 'Summer' or season == 'Autumn':  # проврка през лятото и есента
    amount = 4200  # цена 4200лв
    if fishers_count <= 6:  # проврка до 6 рибаря
        amount = amount * 0.9  # сума с 10% отстъпка
    elif 7 <= fishers_count <= 11:  # проверка между 7 и 11 рибаря
        amount = amount * 0.85  # сума с 15% отстъпка
    elif fishers_count > 12:  # проврка над 12 рибаря
        amount = amount * 0.75  # сума с 25% отстъпка
elif season == 'Winter':  # проврка през зимата
    amount = 2600  # цена 2600лв
    if fishers_count <= 6:  # проврка до 6 рибаря
        amount = amount * 0.9  # сума с 10% отстъпка
    elif 7 <= fishers_count <= 11:  # проверка между 7 и 11 рибаря
        amount = amount * 0.85  # сума с 15% отстъпка
    elif fishers_count > 12:  # проврка над 12 рибаря
        amount = amount * 0.75  # сума с 25% отстъпка

if fishers_count % 2 == 0 and not season == 'Autumn':  # проверка за допънителна отстъпка
    amount = amount * 0.95  # допълнителна отстъпка от 5%

if budget >= amount:  # проверка за бюджет
    rest_money = budget-amount  # остатък от бюджета
    print(f'Yes! You have {rest_money:.2f} leva left.')  # отпечатване при достатъчен бюджет
else:  # проверка за бюджет
    needed_money = amount-budget  # недостиг към бюджета
    print(f'Not enough money! You need {needed_money:.2f} leva.')  # отпечатване при неодстиг
