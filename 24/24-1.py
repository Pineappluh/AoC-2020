import fileinput
from collections import defaultdict


def get_direction(current_pos, cardinal_direction):
    odd_row = (current_pos[0] % 2) != 0
    if cardinal_direction == 'e':
        return 0, 1
    elif cardinal_direction == 'w':
        return 0, -1
    elif cardinal_direction == 'nw':
        return -1, 0 if odd_row else -1
    elif cardinal_direction == 'ne':
        return -1, 1 if odd_row else 0
    elif cardinal_direction == 'sw':
        return 1, 0 if odd_row else -1
    elif cardinal_direction == 'se':
        return 1, 1 if odd_row else 0


def flip(tiles, line, pos=(0, 0)):
    i = 0
    while i < len(line):
        cardinal = line[i]
        cardinal_next = '' if i + 1 >= len(line) else line[i + 1]

        if cardinal + cardinal_next in ['nw', 'ne', 'sw', 'se']:
            direction = get_direction(pos, cardinal + cardinal_next)
            i += 2
        else:
            direction = get_direction(pos, cardinal)
            i += 1

        pos = (pos[0] + direction[0], pos[1] + direction[1])

    tiles[pos] = (tiles[pos] + 1) % 2


lines = []
for line in fileinput.input():
    lines.append(line.strip())

tiles = defaultdict(int)

for line in lines:
    flip(tiles, line)

print(list(tiles.values()).count(1))
