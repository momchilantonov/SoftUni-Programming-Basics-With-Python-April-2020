from math import pi

type_of_figure = input()

if type_of_figure == 'square':
    side_a_square = float(input())
    square_area = side_a_square * side_a_square
    print(f'{square_area:.3f}')
elif type_of_figure == 'rectangle':
    side_a_rectangle = float(input())
    side_b_rectangle = float(input())
    rectangle_area = side_a_rectangle * side_b_rectangle
    print(f'{rectangle_area:.3f}')
elif type_of_figure == 'circle':
    radius_of_circle = float(input())
    circle_area = pi * radius_of_circle ** 2
    print(f'{circle_area:.3f}')
elif type_of_figure == 'triangle':
    side_a_triangle = float(input())
    height_h_triangle = float(input())
    triangle_area = ((side_a_triangle * height_h_triangle) / 2)
    print(f'{triangle_area:.3f}')
