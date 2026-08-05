"""nnnnnnnnnn"""
x = int(input())
y = int(input())
z = int(input())

even = 0
odd = 0
if not x % 2 :
    even+=1
if not y % 2 :
    even+=1
if not z % 2 :
    even+=1
if x % 2:
    odd+=1
if y % 2:
    odd+=1
if z % 2:
    odd+=1
print(even)
print(odd)
