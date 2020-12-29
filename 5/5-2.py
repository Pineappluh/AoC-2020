import fileinput
from collections import defaultdict


def decode(seat):
    encoded_row = seat[:7]
    encoded_row = encoded_row.replace("F", "0")
    encoded_row = encoded_row.replace("B", "1")
    row = int(encoded_row, 2)

    encoded_col = seat[7:]
    encoded_col = encoded_col.replace("L", "0")
    encoded_col = encoded_col.replace("R", "1")
    col = int(encoded_col, 2)

    return row, col


flight = defaultdict(list)
for line in fileinput.input():
    row, col = decode(line.strip())
    flight[row].append(col)

keys = sorted(flight)
for key in keys:
    print(key, sorted(flight[key]))
