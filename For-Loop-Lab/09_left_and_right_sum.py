qty_num = int(input())

first_nums = 0
second_nums = 0

for loop_index in range(0, qty_num * 2):
    loop_num = int(input())
    if loop_index < qty_num:
        first_nums += loop_num
    elif loop_index >= qty_num:
        second_nums += loop_num

if first_nums == second_nums:
    print(f'Yes, sum = {first_nums}')
else:
    diff_nums = abs(first_nums-second_nums)
    print(f'No, diff = {diff_nums}')
