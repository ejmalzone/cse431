# Your code goes here.
player_count = int(input())
players = [int(n) for n in input().split()]

while players:
    print(len(players))

    least = min(players)
    players = [player - least for player in players if player > least]
