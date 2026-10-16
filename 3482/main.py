"""nnnnnnn"""

queue = [
    ("Spider Demon", 1),
    ("Swamp Demon", 2),
    ("Arrow Demon", 1),
    ("Hand Demon", 2),
    ("Drum Demon", 3),
    ("Mugen Train", 2),
    ("Upper Moon", 3)
]

kills = 0
total = 0

while kills < 5:
    name, ans = queue.pop(0)
    print(name)

    i = 0
    passed = False

    while i < 2:
        try:
            x = int(input())
        except EOFError:
            break

        total += 1
        i += 1

        if x == ans:
            print("kill")
            kills += 1
            passed = True
            break

    if kills == 5:
        break

    if not passed:
        print("back")
        queue.append((name, ans))

print(total)
