"""nnnnnnn"""
x = int(input())
total = 0

while True:
    y = int(input())
    if y == -1:
        break
    total += y
    if total == x:
        break

print(total)
