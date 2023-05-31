bps = []
minerals = {
    'ore': 0,
    'clay': 0,
    'obs': 0,
    'geode': 0,
    'pause': 0
    }

robots = {
    'ore': 1,
    'clay': 0,
    'obs': 0,
    'geode': 0,
    'pause': 0
}

max_geode = 0

with open('input.txt') as f:
    for bp in f:
        bp = bp.strip().split()
        bp = {
            'num': int(bp[1][:-1]),
            'ore': (int(bp[6]), 0, 0),
            'clay': (int(bp[12]), 0, 0),
            'obs': (int(bp[18]), int(bp[21]), 0),
            'geode': (int(bp[27]), 0, int(bp[30])),
            'pause': (0, 0, 0)
            }
        bps.append(bp)

def mine_geode(bp, minerals, robots, timer):

    global max_geode
     
    if timer > 23:
        if minerals['geode'] > max_geode:
            max_geode = minerals['geode']
            print(max_geode)
        return

    for build in ('ore', 'clay', 'obs', 'geode', 'pause'): #build
        for robot, mineral in robots.items(): #yield
            minerals[robot] += mineral
        if bp[build][0] <= minerals['ore'] and bp[build][1] <= minerals['clay'] and bp[build][2] <= minerals['obs']:
            timer += 1
            minerals['ore'] -= bp[build][0]
            minerals['clay'] -= bp[build][1]
            minerals['obs'] -= bp[build][2]
            robots[build] += 1
            mine_geode(bp, minerals, robots, timer)
            minerals['ore'] += bp[build][0]
            minerals['clay'] += bp[build][1]
            minerals['obs'] += bp[build][2]
            robots[build] -= 1
            timer -= 1
        for robot, mineral in robots.items(): #unyield
            minerals[robot] -= mineral

mine_geode(bps[0], minerals, robots, 1)
print(max_geode)
