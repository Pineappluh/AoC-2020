def get_pick_up(puzzle, current):
    pick_up = []
    for i in range(3):
        current = puzzle[current]
        pick_up.append(current)
    return pick_up


def get_destination(puzzle, current, pick_up):
    dest = current

    while True:
        if dest > 1:
            dest -= 1
        else:
            dest = len(puzzle)

        if dest not in pick_up:
            break

    return dest


def make_move(puzzle, current, pick_up, dest):
    puzzle[current] = puzzle[pick_up[2]]
    dest_next = puzzle[dest]
    puzzle[dest] = pick_up[0]
    puzzle[pick_up[2]] = dest_next
    return puzzle


puzzle_list = list(map(int, "469217538"))

for i in range(10, 1000000 + 1):
    puzzle_list.append(i)

puzzle = dict()
for el, next_el in zip(puzzle_list, puzzle_list[1:] + [puzzle_list[0]]):
    puzzle[el] = next_el

current = puzzle_list[0]

for i in range(10000000):
    pick_up = get_pick_up(puzzle, current)
    dest = get_destination(puzzle, current, pick_up)
    puzzle = make_move(puzzle, current, pick_up, dest)
    current = puzzle[current]

first_star = puzzle[1]
second_star = puzzle[first_star]
print(first_star, second_star, first_star * second_star)

