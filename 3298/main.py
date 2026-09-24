"""nnnnnnnnnn"""
x = input()
y = x.lower()

if "buu" in y:
    n = 0

    for i, char in enumerate(y):
        if char == "b":
            j = i + 1
            count = 0

            while j < len(y) and y[j] == "u":
                count += 1
                j += 1

            if count > n:
                n = count

    print("Yes", n)

elif "b" in y:
    n = y.index("b")
    print(x[:n + 1] + "U" * (len(x) - n - 1))

else:
    print(("BUU" * len(x))[:len(x)])
