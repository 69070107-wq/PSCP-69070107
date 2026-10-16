"""nnnn"""
a = tuple(input().split())
b = input()

x = a.index(b)
y = a.count(b)

for _ in range(y):
    print(*[x] * y)
