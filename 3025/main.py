"""nnn"""
x = int(input())
y = int(input())

if x in (1,2,3):
    if y >= 21 and x == 3 :
        print("spring")
    else: print("winter")
elif x in (4,5,6) :
    if y >= 21 and x == 6 :
        print("summer")
    else: print("spring")
elif x in (7,8,9):
    if y >= 21 and x == 9 :
        print("fall")
    else:print("summer")
elif x in (10,11,12):
    if y >= 21 and x == 12:
        print("winter")
    else:print("fall")
