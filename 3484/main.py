"""nnnnn"""
n, p = map(int, input().split())
a = []
row = [0] * n
col = [0] * n
row_p = [0] * n
col_p = [0] * n
total = 0
count = 0

for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if a[i][j] > 0:
            row[i] += 1
            col[j] += 1
            count += 1
        row_p[i] += a[i][j]
        col_p[j] += a[i][j]
        total += a[i][j]

for i in range(n):
    print(*a[i], row[i], row_p[i])

print(*col)
print(*col_p)
print(count, total, f"{total * p:.2f}")
