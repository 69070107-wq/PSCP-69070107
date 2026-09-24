"""nnnnnn"""
w, l, m, n = map(int, input().split())
ans = w * l

for a in range(m, n + 1):
    use1 = w * (l // a) * a
    use2 = (w // a) * a * (l % a)

    left = w * l - use1 - use2

    if left < ans:
        ans = left

print(ans)
