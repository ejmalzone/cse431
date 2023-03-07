job_count = int(input())

jobs = []

for i in range(job_count):
    arrival_time, duration = map(int, input().split())
    jobs.append((arrival_time, duration))

jobs.sort(key=lambda m: m[0], reverse=True)

while jobs:
