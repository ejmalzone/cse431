# Your code goes here.
t = int(input())
vals = []

for i in range(t):
    vals.append(tuple(int(n) for n in input().split()))

for ideas, ideas_per_game, games_per_bonus in vals:
    total_games = 0

    leftover_games = ideas // ideas_per_game
    total_games += leftover_games
    bonus_games = None

    while bonus_games != 0:
        bonus_games, leftover_games = divmod(leftover_games, games_per_bonus)
        total_games += bonus_games
        leftover_games += bonus_games

    print(total_games)