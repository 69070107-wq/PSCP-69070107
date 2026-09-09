"""nnnnnnnnnn"""
x,y = map(int, input().split())
n = 0
while y > 0 and x >= 1:
    y -=x
    x -=2
    n +=1

if y >= 1 :
    print("-1")
else:
    print(n)
