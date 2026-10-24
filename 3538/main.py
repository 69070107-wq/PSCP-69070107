"""nnnnnnn"""
s = input()
a = ""

for i in s:
    if s.count(i) % 2 == 1 and i not in a:
        a += i

if not a:
    print("fully paired")
else:
    print(a)
