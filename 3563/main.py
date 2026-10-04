"""nnn"""
x = input().replace("0", "")
n = 1

for i in x:
    n *= int(i)

if not x:
    print(0)
else:
    print(n)
