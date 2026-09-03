"""nnnnnn"""
text = input()
x = 0
y = 0
for ch in text:
    if ch == 'N':
        y+=1
    elif ch == 'S':
        y-=1
    elif ch == 'E':
        x+=1
    elif ch == 'W':
        x-=1
print(f"{x} {y} {abs(x) + abs(y)}")
