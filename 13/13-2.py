import fileinput

busses = []
for line in fileinput.input():
    data = line.split(",")
    for i, bus in enumerate(data):
        if bus != 'x':
            busses.append((i, int(bus)))

factor = 100000000000000 // busses[0][1]
while True:
    t = busses[0][1] * factor
    for delay, bus in busses:
        delayed_t = t + delay
        if delayed_t % bus != 0:
            break
    else:
        print(t)
        break

    factor += 1
