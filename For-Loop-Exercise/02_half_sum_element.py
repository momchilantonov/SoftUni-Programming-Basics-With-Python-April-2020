import sys

numbers = int(input())

sum_numbers = 0
max_number = -sys.maxsize

for i in range(numbers):
    input_numbers = int(input())
    sum_numbers += input_numbers
    if input_numbers > max_number:
        max_number = input_numbers

new_sum_numbers = sum_numbers - max_number

if new_sum_numbers == max_number:
    print('Yes')
    print(f'Sum = {new_sum_numbers}')
else:
    diff = max_number - new_sum_numbers
    print('No')
    print(f'Diff = {abs(diff)}')
