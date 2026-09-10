"""nnnnn"""
a , b = input().split()
c , d = input().split()
money = 0
if a == c and b == d:
    money = 1000000
elif b == d:
    money = 100000
elif a == c and b[-3:] == d[-3:]:
    money = 2000
elif a == c and b[-2:] == d[-2:]:
    money = 1000
elif b[-3:] == d[-3:]:
    money = 200
elif b[-2:] == d[-2:]:
    money = 100
elif a == c:
    money = 20

print(money)
