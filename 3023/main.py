"""nnnn"""
n = int(input())
x = 0

if n == 1 :
    print("1")
elif n != 1 :
    for i in range(n):
        x += len(str(i+1))
        x+=1
    print(x)
