# Your code goes here.
t = int(input())
vals = []

for i in range(t):
    x, y, n = [int(a) for a in input().split()]
    vals.append((x, y, n))

for x, y, n in vals:
    def branch(roots):
        ret = []

        for root in roots:
            ret.extend([root + x, root + y])

        return ret

    current_scores = [x, y]
    total_scores = []

    for i in range(n - 1):
        current_scores = branch(current_scores)

    print(' '.join(map(str, sorted(list(set(current_scores))))))
