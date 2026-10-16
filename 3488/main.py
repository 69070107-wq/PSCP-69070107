
"""nnnnnnnnn"""

n = int(input())
x = [False] * 360

j = 0
while j < n:
    d1 = input().split()
    a = int(d1[0])
    b = int(d1[1])

    if a < b:
        i = a
        while i < b:
            x[i] = True
            i += 1
    else:
        i = a
        while i < 360:
            x[i] = True
            i += 1

        i = 0
        while i < b:
            x[i] = True
            i += 1

    j += 1

full = True
i = 0
while i < 360:
    if not x[i]:
        full = False
        break
    i += 1

if full:
    print(360)
else:
    y = x + x
    mx = 0
    cnt = 0
    i = 0

    while i < 720:
        if y[i]:
            cnt += 1
            if cnt > mx:
                mx = cnt
        else:
            cnt = 0
        i += 1

    print(mx)
