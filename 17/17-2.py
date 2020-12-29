import fileinput
from collections import defaultdict


def new_state(x, y, z, w, dimension):
    active_neighbors = get_neighbors(x, y, z, w, dimension)

    if dimension[(x, y, z, w)] == '.' and active_neighbors == 3:
        return '#'

    if dimension[(x, y, z, w)] == '#' and not (active_neighbors == 2 or active_neighbors == 3):
        return '.'

    return dimension[(x, y, z, w)]


def get_neighbors(x, y, z, w, dimension):
    active_neighbors = 0

    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            for k in range(z - 1, z + 2):
                for l in range(w - 1, w + 2):
                    if not (i == x and j == y and k == z and w == l) and dimension[(i, j, k, l)] == '#':
                        active_neighbors += 1

    return active_neighbors


dimension = defaultdict(lambda: '.')

min_x, max_x, min_y, max_y, min_z, max_z, min_w, max_w = -1, 1, -1, 1, -1, 1, -1, 1
for x, line in enumerate(fileinput.input()):
    max_x = max(x + 1, max_x)
    line = line.strip()
    for y, cube in enumerate(line):
        max_y = max(y + 1, max_y)
        if cube == '#':
            dimension[(x, y, 0, 0)] = '#'

for _ in range(6):
    new_dimension = dimension.copy()
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            for z in range(min_z, max_z + 1):
                for w in range(min_w, max_w + 1):
                    new_dimension[(x, y, z, w)] = new_state(x, y, z, w, dimension)

    dimension = new_dimension
    min_x -= 1
    max_x += 1
    min_y -= 1
    max_y += 1
    min_z -= 1
    max_z += 1
    min_w -= 1
    max_w += 1

print(list(dimension.values()).count('#'))
