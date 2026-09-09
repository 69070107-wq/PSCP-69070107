"""nnn"""
x = int(input())
y = int(input())
z = int(input())
t = x+y
if z >= 3 :
    t *=1.5
    print(int(t))
else:print(t)


if t >= 1500 :
    print("5")
    if z >= 7 :
        print("99")
    else:
        print("0")
elif t >= 1000 :
    print("4")
    if y > 300 :
        print("88")
    else:print("0")
elif t >= 500 :
    print("3")
    print("0")
elif t >= 200 :
    print("2")
    print("0")
elif t < 200 :
    print("1")
    print("0")
