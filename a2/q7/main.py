operation_count = int(input())

numbers = []


def print_median(ns):
    if not numbers:
        print('Wrong!')
        return

    elif len(numbers) == 1:
        print(numbers[0])
        return

    mid = len(ns) // 2
    if len(ns) % 2 == 1:
        print(ns[mid])

    else:
        m = (ns[mid - 1] + ns[mid]) / 2
        print(int(m) if int(m) == m else m)


for i in range(operation_count):
    operation, n = input().split()
    n = int(n)

    if operation == 'a':
        numbers.append(n)

    elif operation == 'r':
        try:
            numbers.remove(n)
        except ValueError:
            print('Wrong!')
            continue

    numbers.sort()
    print_median(numbers)
