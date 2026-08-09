"""nnnnnnnn"""
distance = int(input())
money = 35
if distance == 1 :
    print(35)
elif 1 < distance <= 10 :
    money += (distance-1)*5
    print(money)
elif distance >= 11:
    money += 9*5
    money += (distance-10)*8
    print(money)
else:
    print("0")
