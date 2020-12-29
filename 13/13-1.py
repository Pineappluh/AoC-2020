import fileinput

i = 0
goal, busses = None, None
for line in fileinput.input():
    if i == 0:
        goal = int(line.strip())
        i += 1
    else:
        busses = list(map(lambda x: int(x), filter(lambda x: x != 'x', line.split(","))))

min_distance, min_bus = float("+inf"), None
for bus in busses:
    factor = goal // bus
    closest_to_goal = (factor * bus + bus) - goal

    if closest_to_goal < min_distance:
        min_distance = closest_to_goal
        min_bus = bus

print(min_distance, min_bus)
print(min_distance * min_bus)
