number = float(input())
input_number = input()
output_number = input()

new_number = 0

if input_number == 'mm':
    if output_number == 'm':
        new_number = number / 1000
    elif output_number == 'cm':
        new_number = number / 10
elif input_number == 'cm':
    if output_number == 'mm':
        new_number = number * 10
    elif output_number == 'm':
        new_number = number / 100
elif input_number == 'm':
    if output_number == 'mm':
        new_number = number * 1000
    elif output_number == 'cm':
        new_number = number * 100

print(f'{new_number:.3f}')
