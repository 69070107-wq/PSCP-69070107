"""nnnnnnn"""
import math
x1 = int(input())
y1 = int(input())
z1 = int(input())
t1 = int(input())
x2 = int(input())
y2 = int(input())
t2 = int(input())
z2 = int(input())
x = x1/x2
y = y1/y2
z = z1/z2
t = t1/t2
print(math.ceil(max(x,y,z,t)))
