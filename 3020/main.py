"""nnn"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())
x = 0
y = 0
if b == 0 :
    print(a*d)
else:
    for i in range(d):
        if i % b == 0 :
            if i == 0 :
                x +=a
            else:
                x += c
        else:
            x +=a
    print(x)
