"""nnnn"""
x = int(input())
y = input()
z = input()
n = 0
for i in range(x) :
    if int(y[i]) + int(z[i]) != 9:
        n +=1
if not n :
    print("YES")
else:
    print(f"NO {n}")
