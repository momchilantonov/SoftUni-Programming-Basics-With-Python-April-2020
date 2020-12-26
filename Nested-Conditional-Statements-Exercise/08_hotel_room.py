month = input()  # May, June, July, August, September или October
nights_count = int(input())  # бр. нощувки - цяло число

total_price_for_apartment = 0  # обща цена за апартамент
total_price_for_studio = 0  # обща цена за студио

if month == 'May' or month == 'October':  # проверка на цена през м.Май и м.Октомври
    price_apartment = 65 * nights_count  # апартамент – 65 лв./нощувка
    price_studio = 50 * nights_count  # студио – 50 лв./нощувка
    if nights_count <= 7:  # проверка при нощувки между 0 и 7 дни
        total_price_for_studio = price_studio  # обща цена за студио
        total_price_for_apartment = price_apartment  # обща цена за апартамент
    elif nights_count <= 14:  # проверка при нощувки между 7 и 14 дни
        total_price_for_studio = price_studio * 0.95  # обща цена за студио с 5% отстъпка
        total_price_for_apartment = price_apartment  # обща цена за апартамент
    elif nights_count > 14:  # проверка при нощувки над 14 дни
        total_price_for_studio = price_studio * 0.7  # обща цена за студио с 30% отстъпка
        total_price_for_apartment = price_apartment * 0.9  # обща цена за апартамент с 10% отстъпка
elif month == 'June' or month == 'September':  # проверка на цена през м.Юни и м.Септември
    price_apartment = 68.7 * nights_count  # апартамент – 68.70 лв./нощувка
    price_studio = 75.2 * nights_count  # студио – 75.20 лв./нощувка
    if nights_count <= 14:  # проверка при нощувки между 7 и 14 дни
        total_price_for_studio = price_studio  # обща цена за студио
        total_price_for_apartment = price_apartment  # обща цена за апартамент
    elif nights_count > 14:  # проверка при нощувки над 14 дни
        total_price_for_studio = price_studio * 0.8  # обща цена за студио с 20% отстъпка
        total_price_for_apartment = price_apartment * 0.9  # обща цена за апартамент с 10% отстъпка
elif month == 'July' or month == 'August':  # проверка на цена през м.Юли и м.Август
    price_apartment = 77 * nights_count  # апартамент – 77 лв./нощувка
    price_studio = 76 * nights_count  # студио – 76 лв./нощувка
    if nights_count <= 14:  # проверка при нощувки между 0 и 14 дни
        total_price_for_studio = price_studio  # обща цена за студио
        total_price_for_apartment = price_apartment  # обща цена за апартамент
    elif nights_count > 14:  # проверка при нощувки над 14 дни
        total_price_for_studio = price_studio  # обща цена за студио
        total_price_for_apartment = price_apartment * 0.9  # обща цена за апартамент с 10% отстъпка

print(f'Apartment: {total_price_for_apartment:.2f} lv.')  # отпечатване на крайна цена за апартамент
print(f'Studio: {total_price_for_studio:.2f} lv.')  # отпечатване на крайна цена за студио
