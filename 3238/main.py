"""nnnnnnnn"""
# x, y = input().split()
# x = int(x)

# if y == '#':
#     for i in range(x // 2):
#         print("-" * i + y + "-" * (x - 2 - i * 2) + y + "-" * i)

#     if x % 2 == 1:
#         print("-" * (x // 2) + y + "-" * (x // 2))

#     for j in range(x // 2 - 1, -1, -1):
#         print("-" * j + y + "-" * (x - 2 - j * 2) + y + "-" * j)

# else:
#     start = ord(y)

#     for i in range(x // 2):
#         t = chr(start + x // 2 - i)
#         print("-" * i + t + "-" * (x - 2 - i * 2) + t + "-" * i)

#     if x % 2 == 1:
#         print("-" * (x // 2) + y + "-" * (x // 2))

#     for j in range(x // 2):
#         t = chr(start + 1 + j)
#         print("-" * (x // 2 - 1 - j) + t + "-" * (2 * j) + t + "-" * (x // 2 - 1 - j))
s,l = input().split()
s = int(s)
scal = (s//2)+1
arc = ord(l)
for x in range(s):
    for y in range(s):
        if l == '#':
            if y in (x,s-(x+1)):
                print('#', end='')
            else:
                print('-', end='')
        else:
            if y in (x,s-(x+1)):
                print(chr(arc + abs((x+1)-scal)), end='')
            else:
                print('-', end='')
    print()
