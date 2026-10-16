"""nnnn"""
n, s = map(int, input().split())
a = [int(input()) for i in range(n)]

seen = set()
x = s

while x and x not in seen:
    seen.add(x)
    x = a[x - 1]

print(len(seen))
