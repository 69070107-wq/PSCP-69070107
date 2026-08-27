"""nnn"""
num = int(input())
lick = []
dicg = []
oo = 0
for _ in range(num):
    x,y = input().split()
    y = int(y)
    if 15 < y :
        oo+=1
    lick.append(y)
    dicg.append(x)
print(oo)
print(dicg[lick.index(max(lick))])
