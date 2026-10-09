"""nnmnnnn"""
u, a = input().split()
t, b = input().split()
h, c = input().split()

for i in range(1000):
    x = f"{i:03d}"

    def check(n, op, v):
        """nnnnnnn"""
        if op == "==":
            return n == v
        if op == "!=":
            return n != v
        if op == ">":
            return n > v
        if op == "<":
            return n < v
        if op == ">=":
            return n >= v
        return n <= v

    if check(int(x[2]), u, int(a)) and check(int(x[1]), t, int(b)) and check(int(x[0]), h, int(c)):
        print(x)
