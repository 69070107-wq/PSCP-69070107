"""Bus seating"""
n = int(input())
m = int(input())
x = int(input())

for i in range(n - 1, -1, -1):
    row = []
    for j in range(m):
        a = j * n + i + 1
        if a == x:
            row.append("XX")
        else:
            row.append(f"{a:02d}")
    print(" ".join(row))
    if i > 0 and not (n - i) % 2:
        print()
