"""nnnn"""
x = int(input())
z = []
for i in range(x):
    z.append(int(input()))
    i +=i
m = max(z)
print(max(z))
print(z.count(m))