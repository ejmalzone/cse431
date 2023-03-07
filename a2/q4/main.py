outpost_count, guard_count = map(int, input().split())
guard_locations = list(map(int, input().split()))
guard_locations.sort()

if outpost_count != 1:
    greatest_half_distance = -1

    for i in range(1, guard_count):
        distance = guard_locations[i] - guard_locations[i - 1]
        half_distance = distance // 2
        greatest_half_distance = max(greatest_half_distance, half_distance)

    if guard_locations[0] != 0:
        greatest_half_distance = max(greatest_half_distance, guard_locations[0])

    if guard_locations[-1] != (outpost_count - 1):
        greatest_half_distance = max(greatest_half_distance, outpost_count - guard_locations[-1] - 1)

    print(greatest_half_distance)

else:
    print(0)