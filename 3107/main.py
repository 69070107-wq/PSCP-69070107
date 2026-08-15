"""nnnnn"""
yod, year, money = input().split()
year = int(year)
money = int(money)

if yod == 'M':
    bonus = 1500
    if year <= 5:
        bonus += money * 6 / 100
    elif year <= 10:
        bonus += money * 8 / 100
    else:
        bonus += money * 10 / 100
elif yod == 'B':
    bonus = 1000
    if year <= 5:
        bonus += money * 5 / 100
    elif year <= 10:
        bonus += money * 6 / 100
    else:
        bonus += money * 7 / 100
elif yod == 'G':
    bonus = 500
    if year <= 5:
        bonus += money * 4 / 100
    elif year <= 10:
        bonus += money * 5 / 100
    else:
        bonus += money * 6 / 100
print(int(bonus))
