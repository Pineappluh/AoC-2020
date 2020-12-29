import fileinput
import string

count = 0
current_set = set(string.ascii_lowercase)
for line in fileinput.input():
    if line == "\n":
        count += len(current_set)
        current_set = set(string.ascii_lowercase)
    else:
        current_set = current_set.intersection(set(line.strip()))

count += len(current_set)

print(count)
