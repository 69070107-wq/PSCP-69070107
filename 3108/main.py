"""nnnnnnn"""
x,y,z = input().split()

x = int(x)
y = int(y)
z = int(z)

c = x+y+z

x = x * 25
y = y * 40
z = z * 55
t = (x+y+z)*10/100

if c < 3 :
    print(x+y+z)
elif c >= 3 :
    print(int((x+y+z)-t))
