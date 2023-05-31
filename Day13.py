from itertools import zip_longest


def check(s1, s2, res=None):
    for s in zip_longest(s1, s2, fillvalue=-1):

        if res is not None:
            return res


        try:
            if s[0] < s[1]:
                return True
            elif s[0] > s[1]:
                return False
            continue
        except TypeError:
            pass

        
        if isinstance(s[0], int):
            s = ([s[0]], s[1])
        elif isinstance(s[1], int):
            s = (s[0], [s[1]])

        res = check(s[0], s[1], res)

    return res

##signals = []
##total = 0
##
##with open('input13.txt') as f:
##    while True:
##        signal_1 = f.readline().strip()
##        signal_2 = f.readline().strip()
##        f.readline()
##        if signal_1 == '':
##            break
##        signals.append((eval(signal_1), eval(signal_2)))
##
##for n, s in enumerate(signals):
##    if check(s[0], s[1]):
##        total += n+1
##print(total)

signals = []
sorted_signals = [[[2]], [[6]]]

with open('input13.txt') as f:
    for line in f:
        if line.strip():
            signals.append(eval(line.strip()))

for s in signals:
    insert = False
    for n, s_s in enumerate(sorted_signals):
        if check(s, s_s):
            sorted_signals.insert(n, s)
            insert = True
            break
    if not insert:
        sorted_signals.append(s)

print((sorted_signals.index([[2]]) + 1) * (sorted_signals.index([[6]]) + 1))
