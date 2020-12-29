import fileinput
import numpy as np
import math


def match(new_tile, old_tile, match_type):
    if match_type == "UP":
        return np.all(new_tile[0, :] == old_tile[-1, :])
    elif match_type == "LEFT":
        return np.all(new_tile[:, 0] == old_tile[:, -1])


def get_tile_combinations(tile):
    base_tile = tile.copy()
    combinations = []
    for _ in range(2):
        combinations.append(base_tile)
        combinations.append(np.flipud(base_tile))
        combinations.append(np.fliplr(base_tile))
        combinations.append(np.flipud(np.fliplr(base_tile)))

        base_tile = np.rot90(base_tile)

    return combinations


def find_arrangement(tiles, current, used_tiles, arrangement):
    if len(used_tiles) == len(tiles):
        return arrangement

    print(current, [[x[0] if x else x for x in row] for row in arrangement])
    check = [("LEFT", (0, -1)), ("UP", (-1, 0))]
    n = int(math.sqrt(len(tiles)))
    new_pos = (current[0] + (1 if current[1] == n - 1 else 0), (current[1] + 1) % n)
    for tile_name, base_tile in tiles.items():
        if tile_name in used_tiles:
            continue

        for tile in get_tile_combinations(base_tile):
            for direction_name, direction in check:
                pos = (current[0] + direction[0], current[1] + direction[1])
                if not (pos[0] < 0 or pos[1] < 0 or match(tile, arrangement[pos[0]][pos[1]][1], direction_name)):
                    break
            else:
                arrangement[current[0]][current[1]] = (tile_name, tile)
                result = find_arrangement(tiles, new_pos, used_tiles | {tile_name}, arrangement)
                if result:
                    return result
                arrangement[current[0]][current[1]] = None

    return None


tiles = dict()
current_tile = (None, [])
for line in fileinput.input():
    if line == "\n":
        tiles[current_tile[0]] = np.matrix(current_tile[1])
    elif line.startswith("Tile"):
        current_tile = (int(line[5:9]), [])
    else:
        current_tile[1].append(list(line.strip()))

tiles[current_tile[0]] = np.matrix(current_tile[1])

print(len(tiles))
n = int(math.sqrt(len(tiles)))
empty_arrangement = []
for i in range(n):
    empty_arrangement.append([None] * n)

arrangement = find_arrangement(tiles, (0, 0), set(), empty_arrangement)
solution = arrangement[0][0][0] * arrangement[n - 1][0][0] * arrangement[0][n - 1][0] * arrangement[n - 1][n - 1][0]
print(solution)