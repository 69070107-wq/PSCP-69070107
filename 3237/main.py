"""nnnnnn"""
x = int(input())
if x :
    print("0")
    if x > 1 :
        for i in range(x-2):
            print("0",end="")
            print("1"*(i),end="")
            print("0")
        print("0"*x)
