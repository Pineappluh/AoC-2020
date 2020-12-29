import fileinput
import math


def get_forward_movement(angle):
    angle = math.radians(angle)
    return (int(math.cos(angle)), int(math.sin(angle)))


def manhattanDistance(location):
    return abs(location[0]) + abs(location[1])


def get_new_data(start, angle, command):
    action = command[0]
    amount = int(command[1:])
    
    if action == 'N':
        return (start[0], start[1] + amount), angle
    elif action == 'S':
        return (start[0], start[1] - amount), angle
    elif action == 'E':
        return (start[0] + amount, start[1]), angle
    elif action == 'W':
        return (start[0] - amount, start[1]), angle
    elif action == 'L':
        return start, (angle + amount) % 360
    elif action == 'R':
        return start, (angle - amount) % 360
    elif action == 'F':
        direction = get_forward_movement(angle)
        return (start[0] + direction[0] * amount, start[1] + direction[1] * amount), angle
        

angle = 0
location = (0, 0)
for line in fileinput.input():
    line = line.strip()
    location, angle = get_new_data(location, angle, line)

print(manhattanDistance(location))
