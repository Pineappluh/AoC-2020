import fileinput


def verify(target, numbers):
    needed = set()

    for number in numbers:
        if number in needed:
            return True
        needed.add(target - number)

    return False


preamble = 25
numbers = []
for line in fileinput.input():
    numbers.append(int(line.strip()))

current = preamble
while current < len(numbers):
    if not verify(numbers[current], numbers[current - preamble:current]):
        print(numbers[current])
        break

    current += 1

