"""nnnnnnnn"""
a = list(map(int, input().split()))
for i in range(len(a)-1,-1,-1) :
    if a[i] % 3 and a[i] % 5 :
        a.pop(i)

b = a[::-1]
if len(b):
    for j in b :
        print(j)
else:print("Nope")
