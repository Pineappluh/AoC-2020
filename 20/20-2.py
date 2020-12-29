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


def join_arrangement(arrangement):
    row_joined_arrangements = []

    for row in arrangement:
        row_joined_arrangements.append(np.concatenate([x[1][1:-1, 1:-1] for x in row], axis=1))

    return np.concatenate(row_joined_arrangements, axis=0)


def generate_pattern_matrix():
    pattern = "                  # \n#    ##    ##    ###\n #  #  #  #  #  #   ".split("\n")
    matrix = [list(x) for x in pattern]
    return matrix


def matches_pattern(pos, image, pattern_matrix):
    pattern_rows, pattern_columns = len(pattern_matrix), len(pattern_matrix[0])
    n = len(image)
    if pos[0] + pattern_rows > n or pos[1] + pattern_columns > n:
        return False

    for i in range(pattern_rows):
        for j in range(pattern_columns):
            if pattern_matrix[i][j] == "#" and not image[pos[0] + i, pos[1] + j] == "#":
                return False

    return True


def count_patterns(image, pattern_matrix):
    pattern_matches = 0
    n = len(image)

    for i in range(n):
        for j in range(n):
            if matches_pattern((i, j), image, pattern_matrix):
                pattern_matches += 1

    return pattern_matches


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

n = int(math.sqrt(len(tiles)))
empty_arrangement = []
for i in range(n):
    empty_arrangement.append([None] * n)

arrangement = find_arrangement(tiles, (0, 0), set(), empty_arrangement)
image = join_arrangement(arrangement)
pattern_matrix = generate_pattern_matrix()

total_pattern_matches = 0
for possible_image in get_tile_combinations(image):
    total_pattern_matches = max(total_pattern_matches, count_patterns(possible_image, pattern_matrix))
    print(total_pattern_matches)

pattern_hashtags = 15
print(np.count_nonzero(image == '#') - total_pattern_matches * pattern_hashtags)
