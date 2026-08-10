"""nnnnnnn"""
x,y = input().split()
price = 0
if x == 'S':
    if y == 'R':
        price+=60
    elif y == 'T':
        price+=80
elif x == 'M':
    if y == 'R':
        price+=80
    elif y == 'T':
        price+=100
elif x == 'L':
    if y == 'R':
        price+=100
    elif y == 'T':
        price+=120

z = input().split()
if z[0] == 'P':
    price+=int(z[1]) * 15
elif z[0] == 'E':
    price+=int(z[1]) * 10

print(price)
