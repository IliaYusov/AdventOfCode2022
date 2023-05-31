array = []
visited = set()
visit = set()
new_visit = set()
step = 0

with open('input12.txt') as f:
    for x, line in enumerate(f):
        row = []
        for y, letter in enumerate(line.strip()):
            if letter == 'S' or letter == 'a':
                visit.add((x, y))
                row.append(ord('a') - 97)
            elif letter == 'E':
                end = (x, y)
                row.append(ord('z') - 97)
            else:
                row.append(ord(letter) - 97)
        array.append(row)

while end not in visit:
    step += 1
    for loc in visit:
        height = array[loc[0]][loc[1]]
        for d in (loc[0]+1, loc[1]), (loc[0]-1, loc[1]), (loc[0], loc[1]+1), (loc[0], loc[1]-1):
            if d not in visited:
                if 0 <= d[0] <= len(array)-1 and d[1] >= 0 and d[1] <= len(array[0])-1:
                    if array[d[0]][d[1]] - array[loc[0]][loc[1]] <= 1:
                        new_visit.add(d)
    visited = visited.union(visit)
    visit = new_visit
    new_visit = set()

print(step)
