n1 = int(input())
n2 = int(input())
operator = input()  # "+", "-", "*", "/", "%"

if operator == '+':  # проверка при оператор събиране
    the_sum = n1+n2  # сумата на числата
    if the_sum % 2 == 0:  # проверка дали сумата е четна
        print(f'{n1} + {n2} = {the_sum} - even')  # оптечатай резултат
    else:  # ако сумта е нечтна
        print(f'{n1} + {n2} = {the_sum} - odd')  # оптечатай резултат
elif operator == '-':  # проверка при оператор изваждане
    the_subtraction = n1-n2  # разлката между числата
    if the_subtraction % 2 == 0:  # проверка дали сумата е четна
        print(f'{n1} - {n2} = {the_subtraction} - even')  # оптечатай резултат
    else:  # ако сумта е нечтна
        print(f'{n1} - {n2} = {the_subtraction} - odd')  # оптечатай резултат
elif operator == '*':  # проверка при оператор умножение
    the_multiplication = n1 * n2  # умножението на числата
    if the_multiplication % 2 == 0:  # проверка дали сумата е четна
        print(f'{n1} * {n2} = {the_multiplication} - even')  # оптечатай резултат
    else:  # ако сумта е нечтна
        print(f'{n1} * {n2} = {the_multiplication} - odd')  # оптечатай резултат
elif operator == '/':  # проверка при оператор делене
    if n2 == 0:  # проверка дали второто число е равно на 0 (делене на 0)
        print(f'Cannot divide {n1} by zero')  # оптечатай резултат
    else:  # при второто число различно от 0
        the_division = n1 / n2  # делението на числата
        print(f'{n1} / {n2} = {the_division:.2f}')  # оптечатай резултат
elif operator == '%':  # проверка при оператор модулно делене
    if n2 == 0:  # проверка дали второто число е равно на 0 (делене на 0)
        print(f'Cannot divide {n1} by zero')  # оптечатай резултат
    else:  # при второто число различно от 0
        the_residue = n1 % n2  # остатък след модулно дление на числата
        print(f'{n1} % {n2} = {the_residue}')  # оптечатай резултат
