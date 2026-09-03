"""nnnn"""
start, end = map(int, input().split())
prime = []

for num in range(start, end + 1):
    if num < 2:
        continue

    is_prime = True

    for i in range(2, num):
        if not num % i:
            is_prime = False
            break

    if is_prime:
        prime.append(num)
if prime:
    print(*prime)
print(f"Total primes: {len(prime)}")
