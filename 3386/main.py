"""nnnn"""
m = int(input())
n = int(input())
a = []
b = []

for i in range(m):
    a.append(input())

for i in range(n):
    b.append(input())

c = sorted(set(a) & set(b), reverse=True)

if not c:
    print("Nope")
else:
    for i in c:
        print(i)
