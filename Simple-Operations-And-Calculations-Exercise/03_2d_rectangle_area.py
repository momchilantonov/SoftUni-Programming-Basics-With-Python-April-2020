x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())

length = abs(x_1 - x_2)
width = abs(y_1 - y_2)
area = length * width
perimeter = 2 * length + 2 * width

print(f'{area:.2f}')
print(f'{perimeter:.2f}')
