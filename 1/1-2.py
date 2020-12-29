import fileinput

numbers = []
for line in fileinput.input():
    line = line.strip()
    numbers.append(int(line))
    
target = 2020
for x in numbers:
    for y in numbers:
        remaining = target - x - y
        if remaining in numbers:
            print(x * y * remaining)
            break
