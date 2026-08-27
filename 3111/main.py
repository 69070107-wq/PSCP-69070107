"""nnnnnnnnn"""
from decimal import Decimal, ROUND_HALF_UP

member = input()
n = int(input())

total = Decimal("0")

for _ in range(n):
    total += Decimal(input())

if member == "Y":
    total *= Decimal("0.95")
elif member == "N" and total >= Decimal("500"):
    total *= Decimal("0.97")

total = total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

print(total)
