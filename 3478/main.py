"""nnnnnnn"""
s = input()

for i in range(26):
    a = chr(ord('a') + i)
    b = chr(ord('A') + i)
    if a in s:
        print(a, "=", s.count(a), sep=" ")
    if b in s:
        print(b, "=", s.count(b), sep=" ")
