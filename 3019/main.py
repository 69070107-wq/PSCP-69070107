"""skuba"""
x = input()
y = input()

if x != 'H' and y != '4567':
    print("safe locked")
elif x != 'H' and y == '4567':
    print("safe locked - change char")
elif x == 'H' and y != '4567':
    print("safe locked - change digit")
else:
    print("safe unlocked")
