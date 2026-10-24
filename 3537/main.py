
"""nnnnn"""
alive = {}

while True:
    s = input()
    if s == "Start":
        break
    s = s.replace("{", "").replace("}", "").replace('"', "")
    a = s.split(":")
    name = a[0].strip()
    role = a[1].strip()
    alive[name] = role

dead = {}

while True:
    name = input()
    if name == "End":
        break
    if name in alive:
        dead[name] = alive.pop(name)

count = 0
for name, role in alive.items():
    if role == "Impostor":
        count += 1

print(count, "Impostor Remains")
print("***Alive***")
for name, role in sorted(alive.items()):
    print(name, ":", role)

print("***Dead***")
for name, role in sorted(dead.items()):
    print(name, ":", role)
