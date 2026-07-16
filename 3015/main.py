"""nnn"""
x = int(input())
y = int(input())
a = int(input())
z = int(input())

i = z // x
z = z % x

sale = ((i * y) + z) * a
print(sale)
