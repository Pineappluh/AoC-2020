import fileinput

geology_map = []
for line in fileinput.input():
    geology_map.append(line.strip())

direction = [1, 3]
x, y = 0, 0
rows, cols = len(geology_map), len(geology_map[0])

trees_hit = 0
while x < rows:
    if geology_map[x][y] == '#':
        trees_hit += 1

    x, y = x + direction[0], (y + direction[1]) % cols

print(trees_hit)
