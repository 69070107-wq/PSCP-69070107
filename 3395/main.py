"""nnnnn"""
d1 = input().split()
n = int(d1[0])
l = int(d1[1])
l +=n
h = list(map(int, input().split()))
q = list(map(int, input().split()))

mx = [0] * n
m = -1
i = 0

while i < n:
    if h[i] > m:
        m = h[i]
    mx[i] = m
    i += 1

for x in q:
    p = x - 1
    r = 0

    if p > 0:
        t = mx[p - 1]
        if t >= h[p]:
            r = t - h[p] + 1

    print(r)
