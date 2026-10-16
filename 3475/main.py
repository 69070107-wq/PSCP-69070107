"""nnnnnnnnn"""
menu = []

while True:
    s = input()

    if s == "DONE":
        break

    if s == "CLOSED":
        menu.clear()
        break

    if s == "SOMETHING'S WRONG":
        menu.clear()
    elif s.startswith("Can't do: "):
        food = s[10:]
        if food in menu:
            menu.remove(food)
    else:
        food, course = s.rsplit(" #", 1)

        if course == "N":
            menu.append(food)
        else:
            menu.insert(int(course) - 1, food)

print("Full Course:", menu, "Reversed:", menu[::-1])
