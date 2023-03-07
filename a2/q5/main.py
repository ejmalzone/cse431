growth_goal, arrival_time = map(int, input().split())


DEBUG = False

solution = 1

if solution == 0:
    population = 0

    for i in range(arrival_time):
        population += 1

        if DEBUG:
            print('{}: {} '.format(i + 1, population), end='')

        if population >= growth_goal:
            population = 0
            growth_goal *= 2

            if DEBUG:
                print('(hit cap! Start over...)', end='')

        if DEBUG:
            print()

    print(population)

elif solution == 1:
    while arrival_time > growth_goal:
        arrival_time -= growth_goal
        growth_goal *= 2

    print(arrival_time)
