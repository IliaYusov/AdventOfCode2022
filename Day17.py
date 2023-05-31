from itertools import cycle


def predict(cnt, pattern, repeat_search=None):

    start = None
    repeat = None
    repeat_counter = 0
    repeat_set = set()
    repeat_dict = {}
    
    ROCKS = [
        [(2,4), (3,4), (4,4), (5,4)],
        [(3,6), (2,5), (3,5), (4,5), (3,4)],
        [(4,6), (4,5), (2,4), (3,4), (4,4)],
        [(2,4), (2,5), (2,6), (2,7)],
        [(2,5), (3,5), (2,4), (3,4)]
    ]

    stone = set(((0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0)))

    floor = 0

    rocks_cycle = cycle(ROCKS)
    pattern_cycle = cycle(pattern)

    stone_counter = 0

    while stone_counter < cnt:

        stone_counter += 1
        
        rock = next(rocks_cycle)

        down_move = True

        while down_move:
            
            direction = next(pattern_cycle)

            if repeat_search: # проверка повторов камней на начало цикла сдвигов
                repeat_counter += 1
                if repeat_counter % len(pattern) == 1:
                    if tuple(rock) in repeat_set:
                        start = repeat_dict[tuple(rock)]
                        repeat = stone_counter - repeat_dict[tuple(rock)]
                        return start, repeat
                    repeat_set.add(tuple(rock))
                    repeat_dict[tuple(rock)] = stone_counter

            if direction == '>':
                dx = 1
            elif direction == '<':
                dx = -1
            
            side_move = True        
            side_pos = []

            for point in rock: # сдвиг в сторону
                if (point[0] + dx, floor + point[1]) in stone or (point[0] + dx) > 6 or (point[0] + dx) < 0:
                    side_move = False
                    break
                side_pos.append((point[0] + dx, point[1]))

            if side_move:
                rock = side_pos[:]

            down_pos = []
            
            for point in rock: # сдвиг вниз
                if (point[0], floor + point[1] - 1) in stone:
                    down_move = False
                    break
                down_pos.append((point[0], point[1] - 1))

            if down_move:
                rock = down_pos[:]
            else: # если нет сдвига вниз, фиксируем камень и пересчитываем дно стакана
                max_point = 0
                for point in rock:
                    stone.add((point[0],floor + point[1]))
                    max_point = max(max_point, point[1])
                if max_point > 0:
                    floor += max_point
    return(floor)


def main(num_stones):

    with open('input17.txt') as f:
        pattern = f.readline().strip()

    repeat_or_result = predict(num_stones, pattern, repeat_search=True)

    if isinstance(repeat_or_result, int):
        print(repeat_or_result)

    else:
        start, repeat = repeat_or_result

        a = predict(start, pattern)
        b = (predict(repeat + start, pattern) - predict(start, pattern)) * ((num_stones - start) // repeat)
        c = predict(start + (num_stones - start) % repeat, pattern) - predict(start, pattern)

        print(a + b + c)

main(1000000000000)
