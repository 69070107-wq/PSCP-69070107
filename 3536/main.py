"""nnnn"""

n = int(input())
i = 2
prime = True

if n < 2:
    prime = False
else:
    while i <= n ** 0.5:
        if not n % i:
            prime = False
            break
        i += 1

if prime:
    print("YES")
else:
    print("NO")
