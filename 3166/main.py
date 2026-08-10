"""nnnnnnnn"""
x = int(input())
y = 0
dont = False
for _ in range(x):
    z = int(input())
    y +=z
    if z < 50 :
        dont = True
average = y/x
print(f"{average:.1f}")
if not dont and average >= 60 :
    print("PASS")
else: print("FAIL")
