forest = []
visible_trees = set()
views = {}

with open('input.txt') as f:
    for line in f:
        forest.append([int(tree) for tree in line.strip()])

for x in range(1, len(forest) - 1):
    
    high_tree = forest[x][0]
    for y in range(1, len(forest[0]) - 1):
        if forest[x][y] > high_tree:
            high_tree = forest[x][y]
            visible_trees.add((x, y))
            
    high_tree = forest[x][-1]
    for y in range(len(forest[0]) - 1, 0, -1):
        if forest[x][y] > high_tree:
            high_tree = forest[x][y]
            visible_trees.add((x, y))

for y in range(1, len(forest[0]) - 1):
    
    high_tree = forest[0][y]
    for x in range(1, len(forest) - 1):
        if forest[x][y] > high_tree:
            high_tree = forest[x][y]
            visible_trees.add((x, y))

    high_tree = forest[-1][y]
    for x in range(len(forest) - 1, 0, -1):
        if forest[x][y] > high_tree:
            high_tree = forest[x][y]
            visible_trees.add((x, y))

print(len(visible_trees) + 2 * (len(forest) + len(forest[0]) - 2))

for x in range(1, len(forest) - 1):
    for y in range(1, len(forest[0]) - 1):
        high_tree = forest[x][y]
        for vx in range(x + 1, len(forest)):
            if forest[vx][y] >= high_tree or vx == len(forest) - 1:
                views[(x, y)] = views.setdefault((x, y), 1) * abs(x - vx)
                break
        for vx in range(x - 1, -1, -1):
            if forest[vx][y] >= high_tree or vx == 0:
                views[(x, y)] = views.setdefault((x, y), 1) * abs(x - vx)
                break
        for vy in range(y + 1, len(forest[0])):
            if forest[x][vy] >= high_tree or vy == len(forest[0]) - 1:
                views[(x, y)] = views.setdefault((x, y), 1) * abs(y - vy)
                break
        for vy in range(y - 1, -1, -1):
            if forest[x][vy] >= high_tree or vy == 0:
                views[(x, y)] = views.setdefault((x, y), 1) * abs(y - vy)
                break

print(max(views.values()))
