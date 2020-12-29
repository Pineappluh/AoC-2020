import fileinput


def check_valid(ticket, valid_ranges):
    for field in ticket.split(","):
        field = int(field)

        for range_1, range_2 in valid_ranges:
            if range_1[0] <= field <= range_1[1] or range_2[0] <= field <= range_2[1]:
                break
        else:
            return field

    return None


data = [[], [], []]
index = 0

for line in fileinput.input():
    if line == "\n":
        index += 1
    else:
        data[index].append(line.strip())

field_ranges = data[0]
my_ticket = data[1][1]
tickets = data[2][1:]
valid_ranges = []

for row in field_ranges:
    info = row.split(":")[1].strip().split(" ")
    range_1_info = info[0].split("-")
    range_1 = int(range_1_info[0]), int(range_1_info[1])
    range_2_info = info[2].split("-")
    range_2 = int(range_2_info[0]), int(range_2_info[1])
    valid_ranges.append((range_1, range_2))

invalid_field_sum = 0
for ticket in tickets:
    invalid_field = check_valid(ticket, valid_ranges)
    if invalid_field:
        invalid_field_sum += invalid_field

print(invalid_field_sum)
