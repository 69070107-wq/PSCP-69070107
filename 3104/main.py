"""nnnnnnnn"""
age,day = input().split()
age = int(age)
if day != "Wed":
    if 18 >= age >= 5 :
        print("100")
    elif age >= 19 :
        print("150")
    elif age < 5 :
        print("0")
else:
    if 18 >= age >= 5 :
        print("50")
    elif age >= 19 :
        print("75")
    elif age < 5 :
        print("0")
