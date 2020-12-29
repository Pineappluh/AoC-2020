import fileinput
from collections import deque

player_1 = deque([])
player_2 = deque([])
inputting = 1

for line in fileinput.input():
    if line == "\n":
        inputting = 2
        continue

    if not line.startswith("Player"):
        if inputting == 1:
            player_1.append(int(line))
        else:
            player_2.append(int(line))

winner = None
while player_1 and player_2:
    player_1_card, player_2_card = player_1.popleft(), player_2.popleft()
    if player_1_card > player_2_card:
        player_1.append(player_1_card)
        player_1.append(player_2_card)
    else:
        player_2.append(player_2_card)
        player_2.append(player_1_card)

solution = 0
winner = player_1 if len(player_1) > len(player_2) else player_2
for factor, card in enumerate(reversed(winner)):
    solution += (factor + 1) * card
print(solution)
