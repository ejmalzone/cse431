# Your code goes here.
from math import sqrt
from math import ceil
from math import floor


c = int(input())
ranges = []

for i in range(c):
    x, y = input().split()
    ranges.append((int(x), int(y)))

for x, y in ranges:
    d_size = 0
    s_size = 0
    b_size = 0

    m12 = range(12 * ceil(x / 12), y + 1, 12)
    sqs = range(ceil(sqrt(x)), floor(sqrt(y)) + 1)

    d_size = len(m12)
    s_size = len(sqs)

    for n in sqs:
        if ((n ** 2) % 12) == 0:
            b_size += 1

    print(d_size, s_size, b_size)
