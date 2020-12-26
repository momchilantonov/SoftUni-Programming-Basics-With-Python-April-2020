budget = float(input())  # бюджет реално число
season = input()  # сезон - „summer”, “winter”

destination = ''  # дестинажия за екскурзия - “Bulgaria", "Balkans” и ”Europe”
spend_money = 0  # похарчени пари за екскурзията
place_for_rest = ''  # място за почивка (спане) - „Camp” и „Hotel”

if budget <= 100:  # проверка бюджет под 100лв
    destination = 'Bulgaria'  # екскурзия в България
    if season == 'summer':  # проверка при летен сезон
        place_for_rest = 'Camp'  # лятото ще спи на къмпинг
        spend_money = budget * 0.3  # поарчените пари са 30% от бюджета
    elif season == 'winter':  # проверка при зимен сезон
        place_for_rest = 'Hotel'  # зимата ще спи в хотел
        spend_money = budget * 0.7  # поарчените пари са 70% от бюджета
elif budget <= 1000:  # проверка бюджет под 1000лв
    destination = 'Balkans'  # екскурзия на Балканите
    if season == 'summer':  # проверка при летен сезон
        place_for_rest = 'Camp'  # лятото ще спи на къмпинг
        spend_money = budget * 0.4  # поарчените пари са 40% от бюджета
    elif season == 'winter':  # проверка при зимен сезон
        place_for_rest = 'Hotel'  # зимата ще спи в хотел
        spend_money = budget * 0.8  # поарчените пари са 80% от бюджета
elif budget > 1000:  # проверка бюджет над 1000лв
    destination = 'Europe'  # екскурзия в Европа
    spend_money = budget * 0.9  # поарчените пари са 90% от бюджета
    place_for_rest = 'Hotel'  # зимата ще спи в хотел

print(f'Somewhere in {destination}')  # отпечатване дестнация
print(f'{place_for_rest} - {spend_money:.2f}')  # отпечатване място за спане и похарчени пари
