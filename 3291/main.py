"""nnnnnn"""
x = int(input())
y = int(input())
n = y // 2
for i in range(n+1):
    print(" "*(i) + "*"*x)

for i in range(n,0,-1):
    print(" "*(i-1) + "*"*x)
