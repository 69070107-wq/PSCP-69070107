
"""nnnnnn"""

n = int(input())

c = []
i = 0
while i < n:
    d1 = input().split()
    c.append((int(d1[0]), int(d1[1]), int(d1[2])))
    i += 1

x0 = c[0][0]
y0 = c[0][1]
d0 = c[0][2]

dx = -d0
found = False

while dx <= d0 and not found:
    dy2 = d0 * d0 - dx * dx
    dy = int(dy2 ** 0.5)

    if dy * dy == dy2:
        j = 0
        while j < 2 and not found:
            if not j:
                py = y0 + dy
            else:
                py = y0 - dy

            px = x0 + dx
            ok = True
            i = 1

            while i < n:
                xi = c[i][0]
                yi = c[i][1]
                di = c[i][2]

                if (px - xi) ** 2 + (py - yi) ** 2 != di * di:
                    ok = False
                    break
                i += 1

            if ok:
                print(px, py)
                found = True

            j += 1

    dx += 1
