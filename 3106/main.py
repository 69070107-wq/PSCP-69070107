"""nnnnn"""
x = int(input())
xxxx = 0
fivehun = 0
hun = 0

while x > 0 :

    if x >= 1000 :
        x-= 1000
        xxxx += 1
    elif x >= 500 :
        x-=500
        fivehun+=1
    elif x >= 100 :
        x-=100
        hun+=1
    else:
        print("ERROR")
        break
if xxxx and not x:
    print(f"1000 = {xxxx}")
if fivehun and not x:
    print(f"500 = {fivehun}")
if hun and not x:
    print(f"100 = {hun}")
