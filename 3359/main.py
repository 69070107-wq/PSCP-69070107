"""nnnnnn"""
x = int(input())
y = [0]*301
for _ in range(x):
    z = int(input())
    y[z] += 1
print(max(y))
