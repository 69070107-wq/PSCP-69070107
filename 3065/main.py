"""nnnnn"""
x = int(input())

if x < 0 :
    print("Error : Please input positive number")
elif x > 9 or not x:
    print("Error : Out of range")
elif 10 > x > 5 :
    if x == 9 :
        print("IX")
    else:
        print("V",end="")
        print("I"*(x-5))
elif x == 5 :
    print("V")
elif 5 > x > 0 :
    if x == 4 :
        print("IV")
    else:
        print("I"*x)
