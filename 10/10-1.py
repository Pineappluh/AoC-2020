import fileinput
from collections import defaultdict

ratings = []
for line in fileinput.input():
    ratings.append(int(line.strip()))

ratings = sorted(ratings)
differences = defaultdict(int)

for prev, nxt in zip([0] + ratings, ratings):
    differences[nxt - prev] += 1

differences[3] += 1  # 3 higher than last

print(differences[1] * differences[3])
print(differences)
