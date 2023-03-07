# Your code goes here.
count, capacity = map(int, input().split())

ns = []

for i in range(count):
    ns.append(int(input()))

ns.sort()

for i in range(capacity):
    print(ns[-(i + 1)])
