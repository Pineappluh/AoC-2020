import fileinput


def decode(seat):
    encoded_row = seat[:7]
    encoded_row = encoded_row.replace("F", "0")
    encoded_row = encoded_row.replace("B", "1")
    row = int(encoded_row, 2)

    encoded_col = seat[7:]
    encoded_col = encoded_col.replace("L", "0")
    encoded_col = encoded_col.replace("R", "1")
    col = int(encoded_col, 2)

    return row * 8 + col


max_pass_id = -1
for line in fileinput.input():
    max_pass_id = max(max_pass_id, decode(line.strip()))

print(max_pass_id)