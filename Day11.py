monkies = {}

with open('input.txt') as f:
    while True:
        name = f.readline().strip().split()
        items = f.readline().strip().split(':')
        oper = f.readline().strip().split(':')
        test = f.readline().strip().split()
        if_true = f.readline().strip().split()
        if_false = f.readline().strip().split()
        f.readline()

        if name:
            monkies[int(name[-1].rstrip(':'))] = [[int(i) for i in items[1].split(',')], oper[1].strip(), int(test[-1]), int(if_true[-1]), int(if_false[-1]), 0]
        else:
            break

common = 1
for m in monkies.values():
    common *= m[2]

for _ in range(10000):
    for n in range(len(monkies)):
        monkies[n][-1] += len(monkies[n][0])
        while monkies[n][0]:
            old = monkies[n][0].pop()
            exec(monkies[n][1])
            new = new % common
            if new % monkies[n][2] == 0:
                monkies[monkies[n][3]][0].append(new)
            else:
                monkies[monkies[n][4]][0].append(new)


active = []
for m in monkies.values():
    active.append(m[-1])
active.sort()
print(active[-1] * active[-2])
