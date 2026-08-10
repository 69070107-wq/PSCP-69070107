"""nnnn"""
x = int(input())
z = []
even = 0
odd = 0
for _ in range(x):
    z.append(int(input()))

for j in z:
    if not j % 2:
        even+=1
    else:
        odd+=1
print(f"SUM {sum(z)}")
print(f"EVEN {even}")
print(f"ODD {odd}")
