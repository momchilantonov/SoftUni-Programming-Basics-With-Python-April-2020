intellect = int(input())
power = int(input())
gender = input()  # female, male

if intellect >= 80 and power >= 80 and gender == 'female':
    print("Queen Bee")
elif intellect >= 80:
    print("Repairing Bee")
elif intellect >= 60:
    print("Cleaning Bee")
elif power >= 80 and gender == 'male':
    print("Drone Bee")
elif power >= 60:
    print("Guard Bee")
else:
    print("Worker Bee")
