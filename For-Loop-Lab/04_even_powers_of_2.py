num = int(input())

execute = 0

for num in range(0, num + 1):
    if num % 2 == 0:
        execute = 2 ** num
        print(execute)
