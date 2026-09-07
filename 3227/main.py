"""nnnnnn"""
x = input().upper()

rank = x[:-1]
suit = x[-1]
suit_name = ''
rank_name = ''

if suit == 'D':
    suit_name = 'diamonds'
elif suit == 'H':
    suit_name = 'hearts'
elif suit == 'S':
    suit_name = 'spades'
elif suit == 'C':
    suit_name = 'clubs'

if rank == 'A':
    rank_name = 'ace'
elif rank == 'J':
    rank_name = 'jack'
elif rank == 'Q':
    rank_name = 'queen'
elif rank == 'K':
    rank_name = 'king'
else:
    rank_name = rank

print(f"{rank_name} of {suit_name}")
