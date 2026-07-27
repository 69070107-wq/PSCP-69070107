"""nnnnnnnn"""
temp = float(input())
s = input()
a = input()


Celsius = 0
result = 0
if s == "C":
    Celsius = temp
elif s == "K" :
    Celsius = temp -273.15
elif s == "F" :
    Celsius = (temp - 32) * 5 / 9
elif s == "R":
    Celsius = (temp * 5 / 9) - 273.15

if a == "K" :
    result = Celsius + 273.15
elif a == "F" :
    result = Celsius * 9 / 5 + 32
elif a == "R" :
    result = (Celsius + 273.15) * 9 / 5
elif a == "C" :
    result = Celsius
print(f"{result:.2f}")
