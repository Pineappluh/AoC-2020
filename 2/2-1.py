import fileinput


def get_info(line):
    data = line.split()

    range = data[0].split("-")
    minm, maxm = int(range[0]), int(range[1])

    return minm, maxm, data[1][:-1], data[2]


def is_valid(line):
    minm, maxm, letter, string = get_info(line)

    count = string.count(letter)

    return minm <= count <= maxm


valid = 0
for line in fileinput.input():
    line = line.strip()
    if is_valid(line):
        valid += 1


print(valid)
