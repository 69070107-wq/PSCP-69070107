"""nnnn"""
x = int(input())
oo = []
for _ in range(x):
    oo.append(int(input()))

print(f"{sum(oo)}")
print(f"{max(oo)}")
print(f"{min(oo)}")
print(f"{sum(oo)/x:.1f}")
