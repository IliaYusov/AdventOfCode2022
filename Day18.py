stones = set()
voids = set()
steam = set()
sides = 0

def neighbours(data):
    x, y, z = data
    return ((x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1))

def steam_check(cells, checked):
    global steam, stones, voids, sides
    cells_to_check = set()
    for cell in cells:
        for neighbour in neighbours(cell):
            if neighbour in steam:
                steam.add(neighbour)
                return True
            elif neighbour in stones or neighbour in checked:
                continue
            else:
                cells_to_check.add(neighbour)
                checked.add(neighbour)
    if cells_to_check:
        return steam_check(cells_to_check, checked)
    else:
        return False

with open('input18.txt') as f:
    for stone in f:
        stones.add(tuple(int(s) for s in stone.strip().split(',')))

for stone in stones:
    for neighbour in neighbours(stone):
        if neighbour not in stones:
            voids.add(neighbour)
            sides += 1

for x in range(-2, 22):
    for y in range(-2, 22):
        for z in range(-2, 22):
            steam.add((-2, y, z))
            steam.add((21, y, z))
            steam.add((x, -2, z))
            steam.add((x, 21, z))
            steam.add((x, y, -2))
            steam.add((x, y, 21))

voids_to_check = voids.copy()

for void in voids_to_check:
    if steam_check((void,), set()):
        voids.discard(void)

for void in voids:
    for neighbour in neighbours(void):
        if neighbour in stones:
            sides -= 1
            
print(sides)
