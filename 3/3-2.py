import fileinput

geology_map = []
for line in fileinput.input():
    geology_map.append(line.strip())

rows, cols = len(geology_map), len(geology_map[0])

solution = 1
for direction in [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]:
    trees_hit = 0
    x, y = 0, 0

    while x < rows:
        if geology_map[x][y] == '#':
            trees_hit += 1

        x, y = x + direction[0], (y + direction[1]) % cols

    solution *= trees_hit

print(solution)
