# Premiere – премиерна прожекция, на цена 12.00 лева
# Normal – стандартна прожекция, на цена 7.50 лева
# Discount – прожекция за деца, ученици и студенти на намалена цена от 5.00 лева

projection = input()  # вид прожекция
rows_count = int(input())  # брой редове
columns_cont = int(input())  # брой колони

price = 0  # цена за билет !!!

if projection == 'Premiere':  # проверка за премиерна прожекция
    price = 12  # цена за билет премиерна прожекция
elif projection == 'Normal':  # проверка за стандартна прожекция
    price = 7.5  # цена за билет стандартна прожекция
elif projection == 'Discount':  # проверка за прожекция с намаление
    price = 5  # цена за билет прожекция с намаление

total_income = rows_count * columns_cont * price  # сума при пълна зала

print(f'{total_income:.2f}')  # отпечатване
