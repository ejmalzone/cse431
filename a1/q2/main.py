# Your code goes here.
def fix(n):
    while n > 1_000_000:
        n -= 1000000

    while n < 0:
        n += 1000000

    return n


def exploit(n):
    if n % 2 == 0:
        n -= 99
        n = fix(n)
        n *= 3
    else:
        n -= 15
        n = fix(n)
        n *= 2

    return fix(n)


t = int(input())
m = []

for i in range(t):
    s, k = input().split()
    s = int(s)
    k = int(k)

    m.append((s, k))

for s, k in m:
    for i in range(k):
        s = exploit(s)

    print(s)
