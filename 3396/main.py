"""nnnnnn"""
d1 = input().split()
n = int(d1[0])
k = int(d1[1])

s = []
mn = 1000000000000
i = 0
while i < n:
    v = int(input())
    s.append(v)
    if v < mn:
        mn = v
    i += 1

ans = 0
i = 0
while i < n:
    if (k - 1) * s[i] < k * mn:
        ans += 1
    i += 1

print(ans)
