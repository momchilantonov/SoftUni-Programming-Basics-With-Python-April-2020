import math  # импортира се math

year_type = input()  # 'leap', 'normal'
holidays_count = int(input())  # цяло число съдържащо броя на празниците (без събота и неделя)
weekends_count = int(input())  # цяло число съдържащо броя на уикендите в които се пътува до родния град (48 за год)

weekends_games = ((48-weekends_count) * 3) / 4  # съботни игри в София
holidays_games = (holidays_count * 2) / 3  # празнични игри в София
total_games_days = 0  # общо играни дни

if year_type == 'normal':  # проверка дали годината е нормална
    total_games_days = weekends_count+weekends_games+holidays_games  # общо играни дни при нормална година
    print(f'{math.floor(total_games_days)}')  # отпечатване общо играни дни при нормална година
elif year_type == 'leap':  # проверка дали годината е високосна
    total_games_days = (weekends_count+weekends_games+holidays_games) * 1.15  # общо играни дни при нвисокосна година
    print(f'{math.floor(total_games_days)}')  # отпечатване общо играни дни при нвисокосна година
