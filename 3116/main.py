"""nnn"""
name = input()

first = ord(name[0].upper())
last = ord(name[-1].upper())
length = len(name)

data = []
for i in range(10):
    if (i + 1) % 2 == 1:
        x = first + i
    else:
        x = last - i
    x %= length
    if x > 9:
        x %= 10
    data.append(x)
print(*data[2:8])
