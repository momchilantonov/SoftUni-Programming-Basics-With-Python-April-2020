qty_num = int(input())

sum_even_nums = 0
sum_odd_nums = 0

for loop_index in range(qty_num):
    loop_num = int(input())
    if loop_index % 2 == 0:
        sum_even_nums += loop_num
    else:
        sum_odd_nums += loop_num

if sum_even_nums == sum_odd_nums:
    print(f'Yes\nSum = {sum_even_nums}')
else:
    diff = abs(sum_even_nums - sum_odd_nums)
    print(f'No\nDiff = {diff}')
