"""nnn"""
x, y, r  = map(int, input().split())
c = int(input())

x +=x
y +=y
distance = (x + y) * r
price = distance * c

print(distance)
print(price)
