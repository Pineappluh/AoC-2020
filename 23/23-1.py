def get_pick_up(puzzle, current):
    if current + 3 < len(puzzle):
        return puzzle[current + 1:current + 4]
    else:
        rotation = (current + 3) % len(puzzle) + 1
        return puzzle[current + 1:len(puzzle)] + puzzle[:rotation]


def get_destination_index(puzzle, curr_value, pick_up):
    dest_value = curr_value

    while True:
        if dest_value > 1:
            dest_value -= 1
        else:
            dest_value = len(puzzle)

        if dest_value not in pick_up:
            break

    return puzzle.index(dest_value)


def make_move(puzzle, current, destination):
    if current < destination:
        return puzzle[:current + 1] + rotate(puzzle[current + 1:destination + 1], 3) + puzzle[destination + 1:]
    else:
        rotated_middle = rotate(puzzle[:destination + 1] + puzzle[current + 1:], 3)
        return rotated_middle[:destination + 1] + puzzle[destination + 1:current + 1] + rotated_middle[destination + 1:]


def rotate(l, n):
    return l[n:] + l[:n]


puzzle = list(map(int, "469217538"))
current = 0

for i in range(100):
    curr_value = puzzle[current]
    pick_up = get_pick_up(puzzle, current)
    dest = get_destination_index(puzzle, curr_value, pick_up)
    puzzle = make_move(puzzle, current, dest)
    current = (current + 1) % len(puzzle)

splitting_index = puzzle.index(1)
solution = puzzle[splitting_index + 1:] + puzzle[:splitting_index]
print(''.join(map(str, solution)))

