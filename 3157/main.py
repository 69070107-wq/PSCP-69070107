"""nnnnn"""
num = int(input())
num2 = 0
for _ in range(num):
    x = input()
    if x == '+':
        num2 +=10
    elif x == '-':
        num2 -=5
print(num2)
