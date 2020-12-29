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


def black_neighbors(tiles, pos):
    cardinal_directions = ['e', 'w', 'ne', 'nw', 'se', 'sw']
    black_count = 0

    for cardinal in cardinal_directions:
        neighbor_direction = get_direction(pos, cardinal)
        if tiles[(pos[0] + neighbor_direction[0], pos[1] + neighbor_direction[1])] == 1:
            black_count += 1

    return black_count


def update(tiles):
    new_tiles = tiles.copy()
    min_x = min(x[0] for x in new_tiles.keys())
    max_x = max(x[0] for x in new_tiles.keys())
    min_y = min(x[1] for x in new_tiles.keys())
    max_y = max(x[1] for x in new_tiles.keys())

    for i in range(min_x - 1, max_x + 2):
        for j in range(min_y - 1, max_y + 2):
            pos = (i, j)
            color = tiles[pos]
            black_count = black_neighbors(tiles, pos)
            if color == 1 and (black_count == 0 or black_count > 2):
                new_tiles[pos] = 0
            elif color == 0 and black_count == 2:
                new_tiles[pos] = 1

    return new_tiles


lines = []
for line in fileinput.input():
    lines.append(line.strip())

tiles = defaultdict(int)

for line in lines:
    flip(tiles, line)

for i in range(100):
    tiles = update(tiles)

print(list(tiles.values()).count(1))
