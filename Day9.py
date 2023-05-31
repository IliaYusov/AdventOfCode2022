def move_tail(head, tail):
    new_tail = [0, 0]
    if abs(head[0] - tail[0]) > 1 and abs(head[1] - tail[1]) > 1:
        new_tail[0] = (head[0] + tail[0]) // 2
        new_tail[1] = (head[1] + tail[1]) // 2
    elif abs(head[0] - tail[0]) > 1:
        new_tail[0] = (head[0] + tail[0]) // 2
        new_tail[1] = head[1]
    elif abs(head[1] - tail[1]) > 1:
        new_tail[1] = (head[1] + tail[1]) // 2
        new_tail[0] = head[0]
    else:
        new_tail = tail
    return new_tail


head = [0, 0]
tail_1 = [0, 0]
tail_2 = [0, 0]
tail_3 = [0, 0]
tail_4 = [0, 0]
tail_5 = [0, 0]
tail_6 = [0, 0]
tail_7 = [0, 0]
tail_8 = [0, 0]
tail_9 = [0, 0]
trail = set()
 
with open('input.txt') as f:
        

    for command in f:
        
        direction, distance = command.strip().split()
        
        if direction == 'U' or direction == 'D':
            d = 1
        else:
            d = 0

        if direction == 'U' or direction == 'R':
            s = 1
        else:
            s = -1

        for i in range(int(distance)):
            head[d] += s
            tail_1 = move_tail(head, tail_1)
            tail_2 = move_tail(tail_1, tail_2)
            tail_3 = move_tail(tail_2, tail_3)
            tail_4 = move_tail(tail_3, tail_4)
            tail_5 = move_tail(tail_4, tail_5)
            tail_6 = move_tail(tail_5, tail_6)
            tail_7 = move_tail(tail_6, tail_7)
            tail_8 = move_tail(tail_7, tail_8)
            tail_9 = move_tail(tail_8, tail_9)
            trail.add(tuple(tail_9))

print(len(trail))
