counter_full = 0
counter_part = 0

with open('input.txt') as f:
    for line in f:
        groups = line.strip().split('-')
        groups[1:2] = groups[1].split(',')
        groups = [int(i) for i in groups]
        if groups[0] <= groups[2] and groups[1] >= groups[3] or groups[0] >= groups[2] and groups[1] <= groups[3] :
            counter_full += 1
        if groups[1] >= groups[2] and groups[0] <= groups[2] or groups[3] >= groups[0] and groups[2] <= groups[0]:
            counter_part += 1

print(f'full overlap = {counter_full}, partial overlap = {counter_part}')
