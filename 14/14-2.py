import fileinput
from collections import defaultdict


def binary_form(value, length=36):
    return ('{:0' + str(length) + 'b}').format(value)


def decimal_form(bin_value):
    return int(bin_value, 2)


def apply_mask(value, mask):
    bin_value = list(binary_form(value))

    for i, bit in enumerate(mask):
        if bit != '0':
            bin_value[i] = bit

    return "".join(bin_value)


def get_combinations(floating_binary):
    floating = []

    for i, bit in enumerate(floating_binary[::-1]):
        if bit == 'X':
            floating.append(2 ** i)

    floating_binary = floating_binary.replace('X', '0')

    combinations = []
    start_loc = decimal_form(floating_binary)

    for i in range(0, 2 ** len(floating)):
        bin_i = binary_form(i, len(floating))
        curr_loc = start_loc
        for bit, floating_value in zip(list(bin_i), floating):
            if bit == '1':
                curr_loc += floating_value
        combinations.append(curr_loc)

    return combinations


memory = defaultdict(int)
mask = ''
for line in fileinput.input():
    if line.startswith("mask"):
        mask = line.strip().split("=")[1].strip()
    else:
        data = line.strip().split("=")
        memory_loc_value = int(data[0].strip()[4:-1])
        value = int(data[1].strip())
        floating_memory_loc = apply_mask(memory_loc_value, mask)

        for memory_loc in get_combinations(floating_memory_loc):
            memory[memory_loc] = value

print(sum(memory.values()))