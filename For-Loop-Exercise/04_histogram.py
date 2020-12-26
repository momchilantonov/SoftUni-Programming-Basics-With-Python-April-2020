numbers = int(input())

sum_numbers_1 = 0
sum_numbers_2 = 0
sum_numbers_3 = 0
sum_numbers_4 = 0
sum_numbers_5 = 0

for number in range(numbers):
    input_numbers = int(input())
    if input_numbers < 200:
        sum_numbers_1 += 1
    elif 200 <= input_numbers <= 399:
        sum_numbers_2 += 1
    elif 400 <= input_numbers <= 599:
        sum_numbers_3 += 1
    elif 600 <= input_numbers <= 799:
        sum_numbers_4 += 1
    elif input_numbers >= 800:
        sum_numbers_5 += 1

percentage_1 = sum_numbers_1 / numbers * 100
percentage_2 = sum_numbers_2 / numbers * 100
percentage_3 = sum_numbers_3 / numbers * 100
percentage_4 = sum_numbers_4 / numbers * 100
percentage_5 = sum_numbers_5 / numbers * 100

print(f'{percentage_1:.2f}%')
print(f'{percentage_2:.2f}%')
print(f'{percentage_3:.2f}%')
print(f'{percentage_4:.2f}%')
print(f'{percentage_5:.2f}%')
