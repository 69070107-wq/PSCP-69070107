"""mmmmmmmm"""
n = int(input())
a = list(map(int, input().split()))
b = []

for x in a:
    if a.count(x) == 1:
        b.append(x)
        n +=1

b.sort()
print(*b)
