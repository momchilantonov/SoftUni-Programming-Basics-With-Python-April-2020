numbers = int(input())

sum_nums_1 = 0
sum_nums_2 = 0
sum_nums_3 = 0

for number in range(numbers):
    input_numbers = int(input())
    if input_numbers % 2 == 0:
        sum_nums_1 += 1
    if input_numbers % 3 == 0:
        sum_nums_2 += 1
    if input_numbers % 4 == 0:
        sum_nums_3 += 1

percentage_1 = sum_nums_1 / numbers * 100
percentage_2 = sum_nums_2 / numbers * 100
percentage_3 = sum_nums_3 / numbers * 100

print(f'{percentage_1:.2f}%')
print(f'{percentage_2:.2f}%')
print(f'{percentage_3:.2f}%')
