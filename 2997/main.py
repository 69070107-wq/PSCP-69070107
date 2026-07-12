number = int(input())
num2 = int(input())
winner = input()

ea = 1 / (1 + 10**((num2-number)/400))
eb = 1 / (1 + 10**((number-num2)/400))

if winner == 'A':
    print(f"{ea:.2f}")
elif winner == 'B':
    print(f"{eb:.2f}")