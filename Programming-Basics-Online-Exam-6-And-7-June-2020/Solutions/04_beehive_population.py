initial_population = int(input())
years = int(input())

born_bees = 0
dead_bees = 0
migrated_bees = 0
population = initial_population

for i in range(1, years+1):
    population += population // 10 * 2
    if i % 5 != 0:
        population -= population // 20 * 2
    elif i % 5 == 0:
        population -= (population // 50 * 5)
        population -= (population // 20 * 2)

print(f'Beehive population: {population}')
