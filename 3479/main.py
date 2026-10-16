"""nnnnnnn"""
card = input().upper()

rank = {"A": "Ace", "J": "Jack", "Q": "Queen", "K": "King"}
suit = {"D": "Diamonds", "H": "Hearts", "S": "Spades", "C": "Clubs"}

point = card[:-1]
group = card[-1]

point = rank.get(point, point)

print(point, "of", suit[group])
