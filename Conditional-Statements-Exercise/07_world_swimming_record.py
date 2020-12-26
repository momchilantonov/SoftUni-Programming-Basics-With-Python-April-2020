import math

record = float(input())
distance = float(input())
time_per_minute = float(input())

time_for_swimming = distance * time_per_minute
slow = math.floor(distance / 15)
slow_in_time = slow * 12.5
total_time = time_for_swimming + slow_in_time
needed_sec = abs(record - total_time)

if total_time < record:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {needed_sec:.2f} seconds slower.')
