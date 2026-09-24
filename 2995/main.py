"""nnnnnnnnnn"""
x = input().lower()
y = x.lower()

if "buu" in x:
    n = 0
    for i in range(len(x)):
        if x[i] == "b":
            j = i + 1
            count = 0
            while j < len(x) and x[j] == "u":
                count += 1
                j += 1
            if count > n:
                n = count
    print("Yes", n)

elif "b" in x:
    n = x.index("b")
    print(x[:n + 1] + "U" * (len(x) - n - 1))

else:
    print(("BUU" * len(x))[:len(x)])
