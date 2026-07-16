"""nnn"""
x = int(input())
y = (x *10) / 100
if y < 50 :
    y = 50
elif y > 1000 :
    y = 1000
z = x + y
vat = (z *7) / 100
total = z + vat
print(f'{total:.2f}')
