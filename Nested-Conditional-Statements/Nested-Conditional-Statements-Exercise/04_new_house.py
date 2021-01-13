flowers_type = input()  # вид цветя - "Roses"-5, "Dahlias"-3.8, "Tulips"-2.8, "Narcissus"-3 или "Gladiolus"-2.5
flowers_qty = int(input())  # количество цветя
budget = int(input())  # бюджет

amount = 0  # първоначална сума за цветя !!!

if flowers_type == 'Roses':  # проверка за рози
    if flowers_qty > 80:  # проверка за количество над 80бр
        amount = 5 * 0.9  # цена 5лв и отстъпка 10%
    else:  # проверка за количество под 80бр
        amount = 5  # цена 5лв
elif flowers_type == 'Dahlias':  # проверка за далии
    if flowers_qty > 90:  # проверка за количество над 90бр
        amount = 3.8 * 0.85  # цена 3.8лв и отстъпка 15%
    else:  # проверка за количество под 90бр
        amount = 3.8  # цена 3.8лв
elif flowers_type == 'Tulips':  # проверка за лалета
    if flowers_qty > 80:  # проверка за количество над 80бр
        amount = 2.8 * 0.85  # цена 2.8лв и отстъпка 15%
    else:  # проверка за количество под 80бр
        amount = 2.8  # цена 2.8лв
elif flowers_type == 'Narcissus':  # проверка за нарциси
    if flowers_qty < 120:  # проверка за количество под 120бр
        amount = 3 * 1.15  # цена 3лв и надценка 15%
    else:  # проверка за количество над 120бр
        amount = 3  # цена 3лв
elif flowers_type == 'Gladiolus':  # проверка за гладиоли
    if flowers_qty < 80:  # проверка за количество под 80бр
        amount = 2.5 * 1.2  # цена 2.5лв и надценка 20%
    else:  # проверка за количество над 80бр
        amount = 2.5  # цена 2.5лв

total_price = amount * flowers_qty  # крайне сума за цветя

if budget >= total_price:  # проверка за достатъчен бюджет
    rest_of_money = budget-total_price  # остатък пари от бюджет
    print(f'Hey, you have a great garden with {flowers_qty} {flowers_type} and {rest_of_money:.2f} leva left.')
    # отпечатване при достатъчно пари
else:  # проверка за недостиг в бюджет
    needed_money = total_price-budget  # недостатъчни средства
    print(f'Not enough money, you need {needed_money:.2f} leva more.')  # отпечатване при недостиг на пари
