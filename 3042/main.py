"""nnnnnnn"""
n = int(input())
y = []
while True:
    if not n % 10:
        break
    n -=1
for i in range(int(n/10)+1):
    i+=i
    y.append(n)
    n -=10
print(*y)
