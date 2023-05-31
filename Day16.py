import re
import time
from functools import lru_cache


@lru_cache(maxsize=256)
def steps(a, b):
    global pathes
    if a not in pathes or b not in pathes:
        return None
    step = 0
    visited = set()
    now = set()
    now.add(a)
    while b not in now:
        step += 1
        visited.update(now)
        now = set()
        for nod in visited:
            if nod in pathes:
                now.update(pathes[nod])
    return step


def valves(rates, pressure, start, clock):

    global max_pressure

    if not rates:
        max_pressure = max(pressure, max_pressure)
        return

    for node, rate in rates.items():
        new_clock = clock + steps(start, node) + 1
        if new_clock > 30:
            max_pressure = max(pressure, max_pressure)
            continue
        new_rates = rates.copy()
        new_rates.pop(node)
        new_pressure = pressure + rate * (30 - new_clock)
        valves(new_rates, new_pressure, node, new_clock)


def valves_2(rates, pressure, clock, s1, f1, t1, r1, s2, f2, t2, r2, cnt):

    global max_pressure
    
    if not rates:

        time_passed = min(t1, t2)
        clock += time_passed
        t1 -= time_passed
        t2 -= time_passed

        if clock > 26:
            max_pressure = max(pressure, max_pressure)
            return

        if t1 == 0:
            pressure += r1 * (26 - clock)
            time_passed = t2
            clock += time_passed
            
            if clock > 26:
                max_pressure = max(pressure, max_pressure)
                return
            
            pressure += r2 * (26 - clock)
            
        elif t2 == 0:
            pressure += r2 * (26 - clock)
            time_passed = t1
            clock += time_passed
            
            if clock > 26:
                max_pressure = max(pressure, max_pressure)
                return
            
            pressure += r1 * (26 - clock)
            
        max_pressure = max(pressure, max_pressure)
        return

    time_passed = min(t1, t2)
    new_clock = clock + time_passed
    t1 -= time_passed
    t2 -= time_passed

    if new_clock > 26:
        max_pressure = max(pressure, max_pressure)
        return

    for node in rates:

        if cnt <= 1:
            print(node, cnt, max_pressure)
    
        if t1 == 0:
            new_rates = rates.copy()
            new_rates.pop(node)
            new_pressure = pressure + r1 * (26 - new_clock)
            new_r1 = rates[node]
            valves_2(new_rates, new_pressure, new_clock, f1, node, steps(f1, node) + 1, new_r1, s2, f2, t2, r2, cnt + 1)
            continue
        elif t2 == 0:
            new_rates = rates.copy()
            new_rates.pop(node)
            new_pressure = pressure + r2 * (26 - new_clock)
            new_r2 = rates[node]
            valves_2(new_rates, new_pressure, new_clock, s1, f1, t1, r1, f2, node, steps(f2, node) + 1, new_r2, cnt + 1)
            continue

pathes = {}
rates = {}
max_pressure = 0
cnt = 0

with open('input16.txt') as f:

    pattern = re.compile(r'[A-Z]{2}')
    
    for line in f:
        line = line.strip().split(';')
        name = pattern.search(line[0])[0]
        rate = int(line[0].split('=')[1])
        lead = pattern.findall(line[1])
        pathes[name] = lead
        if rate > 0:
            rates[name] = rate


valves_2(rates, 0, 0, '', 'AA', 0, 0, '', 'AA', 0, 0, 0)
print(max_pressure)
