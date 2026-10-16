"""nnnnnn"""
n = int(input())
a = list(map(int, input().split()))
s = input()

pos = a.index(1)
treasure = a.index(2)

for c in s:
    if c == 'L':
        new = pos - 1
    else:
        new = pos + 1

    if new < 0 or new >= n:
        continue

    if new == treasure:
        a[pos] = 0
        a[treasure] = 1
        break

    a[pos] = 0
    a[new] = 1
    pos = new

print(*a)
