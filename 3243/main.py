"""nnnnnn"""
x = int(input())
avg = 0
bb = 0
gg = 0
if x >= 1 :
    for i in range(x):
        o = int(input())
        if not i:
            bb = o
            gg = o
        avg +=o
        if o > bb :
            bb = o
        if o < gg :
            gg = o
    print(f"MIN: {gg:.3f}")
    print(f"MAX: {bb:.3f}")
    print(f"AVG: {(avg/x):.3f}")
