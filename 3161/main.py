"""nnnnnnn"""
x = int(input())
for i in range(1,x+1):
    if i % 5:
        print("*",end="")
    elif not i % 5 :
        print("X",end="")
