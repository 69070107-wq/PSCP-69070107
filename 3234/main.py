"""nnnnnnnn"""
x,y = input().split()
y = int(y)

for i in range(1,y+1):
    if x == 'R':
        if i % 3 == 1 % 3:
            print("Red",end=" ")
        elif i % 3 == 2 % 3 :
            print("Green",end=" ")
        elif i % 3 == 3 % 3 :
            print("Blue",end=" ")
    elif x == 'G':
        if i % 3 == 1 % 3:
            print("Green",end=" ")
        elif i % 3 == 2 % 3 :
            print("Blue",end=" ")
        elif i % 3 == 3 % 3 :
            print("Red",end=" ")
    elif x == 'B':
        if i % 3 == 1 % 3:
            print("Blue",end=" ")
        elif i % 3 == 2 % 3 :
            print("Red",end=" ")
        elif i % 3 == 3 % 3 :
            print("Green",end=" ")
