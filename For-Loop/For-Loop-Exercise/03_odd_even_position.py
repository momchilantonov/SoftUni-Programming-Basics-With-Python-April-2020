import sys  # импортваме "system specific parameters and functions"

n = int(input())  # на входа подаваме колко числа искаме да прочетем

odd_sum = 0  # променлива за сума на нечетните
even_sum = 0  # променлива за сума на четните
even_max = -sys.maxsize  # променлива за макс на четните
even_min = sys.maxsize  # променлива за мин на четните
odd_max = -sys.maxsize  # променлива за макс на нечетните
odd_min = sys.maxsize  # променлива за мин на нечетните

for number in range(1, n+1):  # въртим цикъл от 1 до n+1 (от 1 за да можем да проверим кои са четни)
    input_numbers = float(input())  # въвеждаме числата с които ще се работи (проверява и смята)
    if number % 2 == 0:  # проверка за четни позиции на числата
        even_sum += input_numbers  # прибавяме към променливата за сума на четните всяко число от четна позиция
        if input_numbers > even_max:  # проверяваме кое от числата на четна позиция ще е най - голямо
            even_max = input_numbers  # променливата за макс четно присвоява стойност на най - голямото четно число
        if input_numbers < even_min:  # проверяваме кое от числата на четна позиция ще е най - малко
            even_min = input_numbers  # променливата за мин четно присвоява стойност на най - малкото четно число
    else:  # ако позициите на числата не са четни
        odd_sum += input_numbers  # прибавяме към променливата за сума на нечетните всяко число от нечетна позиция
        if input_numbers > odd_max:  # проверяваме кое от числата на нечетна позиция ще е най - голямо
            odd_max = input_numbers  # променливата за макс нечетно присвоява стойност на най - голямото нечетно число
        if input_numbers < odd_min:  # проверяваме кое от числата на нечетна позиция ще е най - малко
            odd_min = input_numbers  # променливата за мин нечетно присвоява стойност на най - малкото нечетно число

print(f'OddSum={odd_sum:.2f},')  # отпечатваме сумата на нечетните

if odd_min == sys.maxsize:  # проверка дали съществува най - малко нечетно
    print('OddMin=No,')  # ако няма такова отпечтваме No
else:  # ако има такова
    print(f'OddMin={odd_min:.2f},')  # отпечатваме резултат

if odd_max == -sys.maxsize:  # проверка дали съществува най - голямо нечетно
    print('OddMax=No,')  # ако няма такова отпечтваме No
else:  # ако има такова
    print(f'OddMax={odd_max:.2f},')  # отпечатваме резултат

print(f'EvenSum={even_sum:.2f},')  # отпечатваме сумата на четните

if even_min == sys.maxsize:  # проверка дали съществува най - малко четно
    print('EvenMin=No,')  # ако няма такова отпечтваме No
else:  # ако има такова
    print(f'EvenMin={even_min:.2f},')  # отпечатваме резултат

if even_max == -sys.maxsize:  # проверка дали съществува най - голямо четно
    print('EvenMax=No')  # ако няма такова отпечтваме No
else:  # ако има такова
    print(f'EvenMax={even_max:.2f}')  # отпечатваме резултат
