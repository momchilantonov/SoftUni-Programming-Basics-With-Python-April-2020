length = float(input()) * 100
width = float(input()) * 100
side_a = float(input()) * 100
area_dancer = 7040

area_hall = length * width
area_wardrobe = side_a ** 2
area_bench = area_hall / 10
free_space = area_hall - area_wardrobe - area_bench
num_dancers = free_space // area_dancer

print(round(num_dancers))
