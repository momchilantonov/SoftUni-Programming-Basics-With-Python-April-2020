length = int(input())
width = int(input())
height = int(input())
percent_taken_volume = float(input())

percent_taken_volume_index = (1 - (percent_taken_volume / 100))
volume_total = length * width * height
volume_free = volume_total * percent_taken_volume_index
needed_liters = volume_free * 0.001

print(f'{needed_liters:.3f}')
