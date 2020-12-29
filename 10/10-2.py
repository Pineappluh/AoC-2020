import fileinput

ratings = []
for line in fileinput.input():
    ratings.append(int(line.strip()))

ratings = sorted(ratings)

combinations = 1
multiplier = 1
consecutive = 0
for prev, nxt in zip([0] + ratings, ratings[1:] + [ratings[-1] + 3]):
    if nxt - prev == 2:
        multiplier *= 2
        if consecutive >= 2:
            multiplier -= 1
        consecutive += 1
    else:
        combinations *= multiplier
        multiplier = 1
        consecutive = 0

print(combinations)
