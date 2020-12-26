days_to_stay = int(input())  # дни за престой - цяло число
room = input()  # вид помещение - "room for one person", "apartment" или "president apartment"
grade = input()  # оценка за обслужване - "positive" или "negative".

amount_for_nights = 0  # сума за всички нощувки
submit = 0  # междинна сума с включена отстъпка

if room == 'room for one person':  # проверка при единична стая
    amount_for_nights = 18 * (days_to_stay-1)
    submit = amount_for_nights
elif room == 'apartment':  # проверка при апартамент
    amount_for_nights = 25 * (days_to_stay-1)
    if days_to_stay < 10:  # проверка на междинна сума при по малко от 10 дни
        submit = amount_for_nights * 0.7
    elif 10 <= days_to_stay <= 15:  # проверка на междинна сума между 10 и 15 дни
        submit = amount_for_nights * 0.65
    elif days_to_stay > 15:  # проверка на междинна сума при повече от 15 дни
        submit = amount_for_nights * 0.5
elif room == 'president apartment':  # Проверка при президентски апартамент
    amount_for_nights = 35 * (days_to_stay-1)
    if days_to_stay < 10:  # проверка на междинна сума при по малко от 10 дни
        submit = amount_for_nights * 0.9
    elif 10 <= days_to_stay <= 15:  # проверка на междинна сума между 10 и 15 дни
        submit = amount_for_nights * 0.85
    elif days_to_stay > 15:  # проверка на междинна сума при повече от 15 дни
        submit = amount_for_nights * 0.8

total_price = 0  # крайна сума за плащане с бакшиш

if grade == 'positive':  # проврка при добра оценка
    total_price = submit * 1.25
elif grade == 'negative':  # проврка при лоша оценка
    total_price = submit * 0.9

print(f'{total_price:.2f}')  # отпечатваме :)
