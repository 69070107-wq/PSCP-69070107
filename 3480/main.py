"""mmmmmmm"""
n = int(input())
h = list(map(int, input().split()))
count = 0

for i in range(n):
    if not i:
        if n == 1 or h[i] > h[i + 1]:
            count += 1
    elif i == n - 1:
        if h[i] > h[i - 1]:
            count += 1
    elif h[i] > h[i - 1] and h[i] > h[i + 1]:
        count += 1

print(count)
