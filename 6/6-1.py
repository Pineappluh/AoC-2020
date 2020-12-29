import fileinput

count = 0
current_set = set()
for line in fileinput.input():
    if line == "\n":
        count += len(current_set)
        current_set = set()
    else:
        current_set = current_set.union(set(line.strip()))

count += len(current_set)

print(count)
