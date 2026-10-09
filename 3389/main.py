"""nnnnn"""
x = int(input())
for _ in range(x):
    z1, z2, z3 = map(float, input().split())
    result = z1+z2+z3
    print(f"{result:.1f}",end="")
    if result > 50 :
        print(", Overloaded",end="")
    if z1 > 20:
        print(", Check Type Plastic", end="")
    if z2 > 20:
        print(", Check Type Can", end="")
    if z3 > 20:
        print(", Check Type Glass", end="")

    print()
