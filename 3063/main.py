"""nnnnnnn"""
x = input()
y = int(input())

if x == "H" and y == 4567 :
    print("safe unlocked")
elif x != "H" and y == 4567:
    print("safe locked - change char")
elif x == "H" and y != 4567:
    print("safe locked - change digit")
else:print("safe locked")
