"""nnnnnn"""
x = int(input())

r = 0
while x > r**2 :
    r+=1
y = x - (r-1)**2
if not y % 2:
    print(2*r-3)
else:
    print(2*r-2)
