"""nmnn"""
x = int(input())
ten = 0
five = 0
two = 0
one = 0
while True :
    if x >= 10 :
        x-=10
        ten+=1
    elif x >= 5 :
        x-=5
        five+=1
    elif x >= 2 :
        x-=2
        two+=1
    elif x >= 1 :
        x-=1
        one+=1
    elif not x:
        break

print(f"10 = {ten}")
print(f"5 = {five}")
print(f"2 = {two}")
print(f"1 = {one}")
