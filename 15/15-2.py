puzzle_input = "11,0,1,10,5,19"
numbers = [int(x) for x in puzzle_input.split(",")]
last_seen = dict()
last_number = numbers[-1]

for i, number in enumerate(numbers):
    last_seen[number] = (i + 1, None)

for turn in range(len(numbers) + 1, 30000000 + 1):
    recent, before = last_seen[last_number]

    if not before:
        new_number = 0
    else:
        new_number = recent - before

    if new_number not in last_seen:
        last_seen[new_number] = (turn, None)
    else:
        last_seen[new_number] = (turn, last_seen[new_number][0])

    last_number = new_number

print(last_number)