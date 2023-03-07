interactions = int(input())

lab = []

DEBUG = False

for i in range(interactions):
    line = input()

    if line.startswith('1'):
        value = int(line.split()[1])

        if not lab:
            lab.append((value, value))

        else:
            last_largest = lab[-1][1]
            lab.append((value, max(value, last_largest)))

        if DEBUG:
            print('{}: Push an artifact worth {} onto the stack. Current: {}'.format(i, value, lab))

    elif line.startswith('2'):
        lab.pop()

        if DEBUG:
            print('{}: Removed the top of the stack. Current: {}'.format(i, lab))

    elif line.startswith('3'):
        print(lab[-1][1])

        if DEBUG:
            print('{}: Print the maximum element on the stack. (which is {})'.format(i, lab[-1][1]))
