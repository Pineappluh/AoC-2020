import fileinput
from copy import deepcopy


def get_adjecent(grid, i, j):
    directions = [(0, -1), (0, 1), (1, 0), (-1, 0), (-1, 1), (-1, -1), (1, -1), (1, 1)]
    neighbors = []

    for direction in directions:
        x, y = i + direction[0], j + direction[1]
        while 0 <= x < len(grid) and 0 <= y < len(grid[0]):
            if grid[x][y] != '.':
                neighbors.append(grid[x][y])
                break

            x, y = x + direction[0], y + direction[1]

    return neighbors


def get_new_state(grid, i, j):
    neighbors = get_adjecent(grid, i, j)

    if grid[i][j] == 'L' and not '#' in neighbors:
        return '#'
    if grid[i][j] == '#' and neighbors.count('#') >= 5:
        return 'L'

    return grid[i][j]


def print_grid(grid):
    for i in range(len(grid)):
        print(''.join(grid[i]))


def count_occupied(grid):
    return sum(row.count('#') for row in grid)


grid = []
for line in fileinput.input():
    grid.append(list(line.strip()))

while True:
    new_grid = deepcopy(grid)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            new_grid[i][j] = get_new_state(grid, i, j)

    if new_grid == grid:
        break
    else:
        grid = new_grid

print(count_occupied(grid))
