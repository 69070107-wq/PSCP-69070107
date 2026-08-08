"""nnnn"""
temp = int(input())
gate = input().lower()
if gate == 'f' :
    temp = (temp-32)/1.8

if 0 >= temp :
    print("solid")
elif temp >= 100 :
    print("gas")
elif 0 < temp < 100 :
    print("liquid")
