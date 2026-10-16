"""nnnnnnnn"""

s = input()

up = [
    "  *  ",
    " *** ",
    "* * *",
    "  *  ",
    "  *  "
]

down = [
    "  *  ",
    "  *  ",
    "* * *",
    " *** ",
    "  *  "
]

left = [
    "  *  ",
    " *   ",
    "*****",
    " *   ",
    "  *  "
]

right = [
    "  *  ",
    "   * ",
    "*****",
    "   * ",
    "  *  "
]

i = 0
while i < 5:
    j = 0
    while j < len(s):
        if s[j] == "U":
            print(up[i], end=" ")
        elif s[j] == "D":
            print(down[i], end=" ")
        elif s[j] == "L":
            print(left[i], end=" ")
        else:
            print(right[i], end=" ")
        j += 1
    print()
    i += 1
