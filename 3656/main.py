"""nnnnnnnn"""
x = input()
y = 0
for i in x :
    y += int(i)
z = int(x[-3:]) * 10
o = y + z
if o > 9999 :
    o = int(str(o)[-4:])
elif o < 1000:
    o +=1000
print(f"{o:04d}")
