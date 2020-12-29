import fileinput
import math


def rotate(waypoint, angle):
    angle = math.radians(angle)
    cos_value, sin_value = int(math.cos(angle)), int(math.sin(angle))
    x1, y1 = waypoint[0], waypoint[1]
    return x1 * cos_value - y1 * sin_value, x1 * sin_value + y1 * cos_value


def manhattan_distance(location):
    return abs(location[0]) + abs(location[1])


def get_new_data(start, waypoint, command):
    action = command[0]
    amount = int(command[1:])
    
    if action == 'N':
        return start, (waypoint[0], waypoint[1] + amount)
    elif action == 'S':
        return start, (waypoint[0], waypoint[1] - amount)
    elif action == 'E':
        return start, (waypoint[0] + amount, waypoint[1])
    elif action == 'W':
        return start, (waypoint[0] - amount, waypoint[1])
    elif action == 'L':
        return start, rotate(waypoint, amount)
    elif action == 'R':
        return start, rotate(waypoint, -amount % 360)
    elif action == 'F':
        return (start[0] + waypoint[0] * amount, start[1] + waypoint[1] * amount), waypoint
        

angle = 0
location = (0, 0)
waypoint = (10, 1)
for line in fileinput.input():
    line = line.strip()
    location, waypoint = get_new_data(location, waypoint, line)

print(manhattan_distance(location))
