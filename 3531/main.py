"""nnnnnn"""
x = int(input())
z = []
while True :
    y = int(input())
    if not y:
        break
    z.append(y)
z.sort()
for i in range(1,x+1):
    if i not in z:
        print(i)
