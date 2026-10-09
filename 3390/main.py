"""nnnnnn"""
a = []
for _ in range(5):
    y = list(map(int,input().split()))
    a.append(y)

row = -1
col = -1

for i in range(5):
    if sum(a[i]) %2 :
        row = i
for j in range(5):
    total = 0
    for i in range(5):
        total += a[i][j]
    if total % 2 :
        col = j
print(row,col)
