"""nnnn"""
x = input()
y = input()

reverse = int(x[::-1])
z = int(x)
if y == '+' :
    z += int(reverse)
    print(f"{x} + {reverse} = {z}")
elif y == '*' :
    z *= int(reverse)
    print(f"{x} * {reverse} = {z}")
