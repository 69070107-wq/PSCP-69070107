"""nnnnn"""
y = []
while True:
    x = input()
    if x == 'NULL':
        break
    y.append(x)
for i in range(len(y)-1,-1,-1):
    print(y[i])
