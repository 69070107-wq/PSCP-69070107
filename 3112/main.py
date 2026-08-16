"""nnnnnnn"""
x ,y = input().split()
z ,t ,r = input().split()
y = float(y)
r = float(r)

if x == 'H':
    x = 5*y
elif x == 'O':
    x = 3*y
elif x == 'J':
    x = 2*y


if z == 'R':
    if t == '1':
        x += 12 * r
    elif t == '2':
        x += 18 * r
    elif t == '3':
        x += 25 * r
elif z == 'T':
    if t == '1':
        x += 15 * r
    elif t == '2':
        x += 20 * r
    elif t == '3':
        x += 30 * r
elif z == 'M':
    if t == '1':
        x += 10 * r
    elif t == '2':
        x += 15 * r
    elif t == '3':
        x += 20 * r

if x.is_integer():
    print(int(x))
else:
    print(x)
