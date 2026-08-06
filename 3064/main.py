"""nnnnnn"""
from datetime import date
y1 = int(input())
m1 = int(input())
d1 = int(input())
y2 = int(input())
m2 = int(input())
d2 = int(input())

num1 = date(y1,m1,d1)
num2 = date(y2,m2,d2)

time1 = abs((num1 - num2).days)

if time1 <= 7  :
    print("0")
elif num1 < num2 :
    print("1")
elif num2 < num1 :
    print("2")
