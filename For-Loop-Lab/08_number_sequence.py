import sys

qty_num = int(input())
max_num = -sys.maxsize
min_num = sys.maxsize

for loop_index in range(qty_num):
    loop_num = int(input())
    if loop_num < min_num:
        min_num = loop_num
    if loop_num > max_num:
        max_num = loop_num

print(f'Max number: {max_num}')
print(f'Min number: {min_num}')
