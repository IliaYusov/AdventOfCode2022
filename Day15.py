import time

data = []
cover = set()
beacons = set()

with open('input15.txt') as f:
    for line in f:
        s, b = line.strip().split(':')
        sx, sy = s.split(',')
        bx, by = b.split(',')
        s = (int(sx.split('=')[1]), int(sy.split('=')[1]))
        b = (int(bx.split('=')[1]), int(by.split('=')[1]))
        data.append((s, b))
        beacons.add(b)

start_time = time.time()

treshhold = 1000000

for line in range(treshhold + 1):

    on_line = []

    for s, b in data:
        distance = abs(s[0] - b[0]) + abs(s[1] - b[1])
        if distance >= abs(s[1] - line):
            side_one = min(s[0] - (distance - abs(s[1] - line)), treshhold)
            side_two = min(s[0] + (distance - abs(s[1] - line)), treshhold)
            on_line.append(sorted((side_one, side_two)))

    on_line.sort()
    r = on_line[0][1]
    for a in on_line[1:]:
        if a[0] <= r + 1 and a[1] > r:
            r = a[1]
    if r != treshhold:
        print((r + 1) * 4000000 + line)

##beacons_on_line =len([b for b in beacons if b[1] == line])
##print(beacons_on_line)
        
print("--- %s seconds ---" % (time.time() - start_time))
