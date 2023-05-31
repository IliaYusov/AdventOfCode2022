def drop_sand(x, y, sand, floor):
    while True:
        if (x, y + 1) not in sand:
            y += 1
            if y == floor:
                sand.add((x, y - 1))
                return sand, False
        elif (x - 1, y + 1) not in sand and y + 1 != floor:
            x, y = x - 1, y + 1
        elif (x + 1, y + 1) not in sand and y + 1 != floor:
            x, y = x + 1, y + 1
        else:
            sand.add((x, y))
            if y == 0:
                return sand, True
            else:
                return sand, False


stone = set()
sand = set()

with open('input14.txt') as f:
    for line in f:
        bar = []
        for x_y in line.strip().split(' -> '):
            bar.append([int(i) for i in x_y.split(',')])
        start = bar[0]
        for turn in bar[1:]:
            if start[0] == turn[0]:
                x = start[0]
                step = (turn[1]-start[1]) // abs((turn[1]-start[1]))
                if step > 0:
                    begin, end = start[1], turn[1] + 1
                else:
                    begin, end = start[1], turn[1] - 1
                for y in range(begin, end, step):
                    stone.add((x, y))      
            elif start[1] == turn[1]:
                y = start[1]
                step = (turn[0]-start[0]) // abs((turn[0]-start[0]))
                if step > 0:
                    begin, end = start[0], turn[0] + 1
                else:
                    begin, end = start[0], turn[0] - 1
                for x in range(begin, end, step):
                    stone.add((x, y))
            start = turn

sand = stone.copy()

floor = max(i[1] for i in stone) + 2

over = False

while not over:
    sand, over = drop_sand(500, 0, sand, floor)

print(len(sand) - len(stone))

