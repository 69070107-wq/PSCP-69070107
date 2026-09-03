"""nnnnnn"""
num = int(input())
oo = []
for _ in range(num):
    x = int(input())
    y = int(input())
    oo.append(max(x,y))
if num == 1:
    print(oo[0])
else:
    print(" + ".join(map(str,oo)),"=",sum(oo))
