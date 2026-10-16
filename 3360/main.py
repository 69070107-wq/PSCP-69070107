"""nnnnnn"""
w, h, m, n = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
m +=n
x = [0] + x + [w]
y = [0] + y + [h]

a = []
for i in range(1, len(x)):
    for j in range(1, len(y)):
        s = (x[i] - x[i - 1]) * (y[j] - y[j - 1])
        a.append(s)

a.sort(reverse=True)
print(a[0], a[1])
