"""mmmmm"""
n = int(input())
h = []

for _ in range(n):
    h.append(int(input()))

m = 0

if n == 1:
    m = 1
else:
    for i in range(n):
        if not i:
            if h[i] > h[i+1]:
                m += 1
        elif i == n-1:
            if h[i] > h[i-1]:
                m += 1
        elif h[i] > h[i-1] and h[i] > h[i+1]:
            m += 1

print(m)
