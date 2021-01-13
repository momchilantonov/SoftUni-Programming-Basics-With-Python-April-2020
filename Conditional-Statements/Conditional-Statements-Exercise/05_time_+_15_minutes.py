hour = int(input())
minutes = int(input())

time_in_minutes = hour * 60+minutes
time_after_15_minutes = time_in_minutes+15
new_hour = time_after_15_minutes // 60
new_minutes = time_after_15_minutes % 60

if new_hour == 24:
    new_hour = 0

if new_minutes < 10:
    print(f'{new_hour}:0{new_minutes}')
else:
    print(f'{new_hour}:{new_minutes}')
