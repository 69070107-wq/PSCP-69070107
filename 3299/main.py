"""nnnnnn"""
l, n = map(int, input().split())
total = 0
diagonal = 0

while total < n:
    diagonal += 1
    total += diagonal

print((diagonal - 1) // l + 1)
