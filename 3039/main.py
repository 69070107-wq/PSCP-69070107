""""nnn"""
x = int(input())
z = []
for i in range(x):
    i +=0
    z.append(int(input()))
t = z[0]
for j in z :
    if t > j :
        t = j
print(t)
