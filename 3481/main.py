"""nnnnnnnnn"""

d1 = input().split()
l = int(d1[0])
n = int(d1[1])

bridges = []
points = set()
points.add(0)
points.add(l)

i = 0
while i < n:
    d2 = input().split()
    a = int(d2[0])
    b = int(d2[1])
    bridges.append((a, b))
    points.add(a)
    points.add(b)
    points.add(a + 0.5)
    points.add(b - 0.5)
    i += 1

mx = 0
for x in points:
    cnt = 0
    i = 0
    while i < n:
        if bridges[i][0] < x < bridges[i][1]:
            cnt += 1
        i += 1

    if cnt > mx:
        mx = cnt

print(mx)
