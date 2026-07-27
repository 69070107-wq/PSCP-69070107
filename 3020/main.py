"""nnn"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())
x = 0
if not b:
    print(a*d)
else:
    for i in range(d):
        if not i % b :
            if not i :
                x +=a
            else:
                x += c
        else:
            x +=a
    print(x)
