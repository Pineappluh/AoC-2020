import fileinput


def get_info(line):
    data = line.split()

    range = data[0].split("-")
    left, right = int(range[0]), int(range[1])

    return left, right, data[1][:-1], data[2]


def is_valid(line):
    left, right, letter, string = get_info(line)

    left_equal = string[left - 1] == letter
    right_equal = string[right - 1] == letter

    return (left_equal or right_equal) and not (left_equal and right_equal)


valid = 0
for line in fileinput.input():
    line = line.strip()
    if is_valid(line):
        valid += 1


print(valid)
