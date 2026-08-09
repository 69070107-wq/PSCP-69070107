"""nn"""
yod,year,money = input().split()
year = int(year)
money = int(money)


if yod == 'M':
    bonus = 1500
elif yod == 'B':
    bonus = 1000
elif yod == 'G':
    bonus = 500

if yod == 'M':
    if year < 5 :
        bonus += (money*(6/100))
    elif 10 >= year >= 5:
        bonus += (money*(8/100))
    elif year > 10:
        bonus += (money*(10/100))
elif yod == 'B':
    if year < 5 :
        bonus += (money*(5/100))
    elif 10 >= year >= 5:
        bonus += (money*(6/100))
    elif year > 10:
        bonus += (money*(7/100))
elif yod == 'G':
    if year < 5 :
        bonus += (money*(4/100))
    elif 10 >= year >= 5:
        bonus += (money*(5/100))
    elif year > 10:
        bonus += (money*(6/100))
print(int(bonus))
