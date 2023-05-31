def inc_cycle(cycle, x, row):
    
    if cycle % 40 == 0:
        row = ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.']  

    if cycle % 40 <= x+1 and cycle % 40 >= x-1:
        row[cycle % 40] = '#'

    cycle += 1
    
    if cycle % 40 == 0:
        print(''.join(row))

    return cycle, row


cycle = 0
x = 1
row = ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.']

with open('input.txt') as f:
    for line in f:
        command, arg = line.strip().split()[0], line.strip().split()[1:]
        if command == 'addx':
            cycle, row = inc_cycle(cycle, x, row)
            cycle, row = inc_cycle(cycle, x, row)
            x += int(arg[0])
        elif command == 'noop':
            cycle, row = inc_cycle(cycle, x, row)
