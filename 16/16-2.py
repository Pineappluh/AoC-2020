import fileinput


def check_valid(ticket, valid_ranges):
    for field in ticket.split(","):
        field = int(field)

        for range_1, range_2 in valid_ranges.values():
            if range_1[0] <= field <= range_1[1] or range_2[0] <= field <= range_2[1]:
                break
        else:
            return False

    return True


def fits_range(ticket, valid_ranges):
    fits = []

    for field in ticket.split(","):
        field = int(field)

        fits.append(set())
        for name, (range_1, range_2) in valid_ranges.items():
            if range_1[0] <= field <= range_1[1] or range_2[0] <= field <= range_2[1]:
                fits[-1].add(name)

    return fits


data = [[], [], []]
index = 0

for line in fileinput.input():
    if line == "\n":
        index += 1
    else:
        data[index].append(line.strip())

field_ranges = data[0]
my_ticket = [int(x) for x in data[1][1].split(",")]
tickets = data[2][1:]
valid_ranges = dict()

for row in field_ranges:
    info = row.split(":")
    name = info[0]
    range_info = info[1].strip().split(" ")
    range_1_info = range_info[0].split("-")
    range_1 = int(range_1_info[0]), int(range_1_info[1])
    range_2_info = range_info[2].split("-")
    range_2 = int(range_2_info[0]), int(range_2_info[1])
    valid_ranges[name] = (range_1, range_2)

valid_tickets = []
for ticket in tickets:
    if check_valid(ticket, valid_ranges):
        valid_tickets.append(ticket)

possible_fields = []
for ticket in valid_tickets:
    possible_fields.append(fits_range(ticket, valid_ranges))

field_names = ['UNKNOWN'] * len(valid_ranges.keys())
solved = set()

while 'UNKNOWN' in field_names:
    for i, name in enumerate(field_names):
        if name == 'UNKNOWN':
            common_fields = set.intersection(*[x[i] for x in possible_fields]) - solved
            if len(common_fields) == 1:
                solved_field = list(common_fields)[0]
                field_names[i] = solved_field
                solved.add(solved_field)

solution = 1
for i, field_name in enumerate(field_names):
    if field_name.startswith("departure"):
        solution *= my_ticket[i]
print(solution)
