"""nnnnn"""
a = input().strip()
b = input().strip()

if len(a) > len(b):
    b += b[0] * (len(a) - len(b))
elif len(b) > len(a):
    a += a[0] * (len(b) - len(a))

r = ""
w = 0
c = 0
m = 0

for i, char in enumerate(a):
    if char.lower() in "love" or b[i].lower() in "love":
        r += "w"
        w += 1
        c += 1
        if c > m:
            m = c
    else:
        r += "$"
        c = 0

if w % 2:
    r += str(m)
elif "ww" not in r:
    r += "#"

print(r)
