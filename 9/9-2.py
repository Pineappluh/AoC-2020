import fileinput


def verify(target, numbers):
    needed = set()

    for number in numbers:
        if number in needed:
            return True
        needed.add(target - number)

    return False


def find_contigous(target, numbers):
    left, right = 0, 1
    window_sum = numbers[left] + numbers[right]

    while True:
        if window_sum == target:
            return numbers[left:right+1]
        elif window_sum < target:
            right += 1
            window_sum += numbers[right]
        elif window_sum > target:
            window_sum -= numbers[left]
            left += 1


preamble = 25
numbers = []
for line in fileinput.input():
    numbers.append(int(line.strip()))

invalid = None
current = preamble
while current < len(numbers):
    if not verify(numbers[current], numbers[current - preamble:current]):
        invalid = numbers[current]
        break

    current += 1

contigous_range = find_contigous(invalid, numbers)
print(min(contigous_range) + max(contigous_range))
