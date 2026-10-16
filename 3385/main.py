"""ppppp"""
p = int(input())
n = int(input())

stops = [[] for i in range(n + 1)]

for _ in range(n):
    data = list(map(int, input().split()))
    stops[data[0]] = data[1:]

bus = []
total = 0

for stop in range(1, n + 1):
    new_bus = []

    for x in bus:
        if x == stop:
            total += 1
        else:
            new_bus.append(x)

    bus = new_bus

    for x in stops[stop]:
        if x > stop and len(bus) < p:
            bus.append(x)

print(total)
