"""nnnnnn"""
x = []

for i in range(5):
    x.append(input().strip())

n = len(max(x, key=len))

print("*" * (n + 4))

for i in x:
    print("* " + i + " " * (n - len(i)) + " *")

print("*" * (n + 4))
