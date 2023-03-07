file_count = int(input())
ids = list(map(int, input().split()))

ids_ref = sorted(ids)

first_wrong_idx = None

for idx in range(1, len(ids)):
    diff = ids[idx] - ids[idx - 1]

    if diff < 0:
        first_wrong_idx = idx - 1

        # elements are strictly swapped
        if diff == -1:
            pass
