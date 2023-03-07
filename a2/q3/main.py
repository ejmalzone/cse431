from collections import defaultdict

count = int(input())
labs = defaultdict(int)

for i in range(count):
    labs[input()] += 1

print(sorted(labs.keys(), key=lambda n: (labs[n], n))[-1])
