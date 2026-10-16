"""nnnnn"""
n = int(input())
v = []
i = 0
while i < n:
    p, eff = input().split()
    v.append(int(eff))
    i += 1
    p = int(p)+i

ans = 0
mx = -1
i = n - 1
while i >= 0:
    if v[i] < mx:
        ans += 1
    else:
        mx = v[i]
    i -= 1

print(ans)
