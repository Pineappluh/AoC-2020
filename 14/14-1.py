import fileinput
from collections import defaultdict


def binary_form(value):
    return '{:036b}'.format(value)


def decimal_form(bin_value):
    return int(bin_value, 2)


def apply_mask(value, mask):
    bin_value = list(binary_form(value))

    for i, bit in enumerate(mask):
        if bit != 'X':
            bin_value[i] = bit

    return decimal_form("".join(bin_value))


memory = defaultdict(int)
mask = ''
for line in fileinput.input():
    if line.startswith("mask"):
        mask = line.strip().split("=")[1].strip()
    else:
        data = line.strip().split("=")
        memory_location = int(data[0].strip()[4:-1])
        value = int(data[1].strip())
        memory[memory_location] = apply_mask(value, mask)

print(sum(memory.values()))