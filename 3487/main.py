
"""nnnnnnnn"""

n = int(input())

a = []
i = 0
while i < n:
    a.append(int(input()))
    i += 1

i = 0
while i < n:
    j = i + 1
    while j < n:
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
        j += 1
    i += 1

s = 0
total = 0
i = 0

while i < n:
    s += a[i]
    total += s * 2
    i += 1

print(total)
