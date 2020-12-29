import fileinput
from collections import deque


def play_game(player_1, player_2):
    played = set()
    while player_1 and player_2:
        state = (tuple(player_1), tuple(player_2))
        if state in played:
            return 1
        played.add(state)

        player_1_card, player_2_card = player_1.popleft(), player_2.popleft()
        if len(player_1) >= player_1_card and len(player_2) >= player_2_card:
            sub_game_player_1 = deque(list(player_1)[:player_1_card])
            sub_game_player_2 = deque(list(player_2)[:player_2_card])
            round_winner = play_game(sub_game_player_1, sub_game_player_2)
        else:
            round_winner = 1 if player_1_card > player_2_card else 2

        if round_winner == 1:
            player_1.append(player_1_card)
            player_1.append(player_2_card)
        else:
            player_2.append(player_2_card)
            player_2.append(player_1_card)

    return 1 if len(player_1) > len(player_2) else 2


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


solution = 0
winner = player_1 if play_game(player_1, player_2) == 1 else player_2
for factor, card in enumerate(reversed(winner)):
    solution += (factor + 1) * card
print(solution)
