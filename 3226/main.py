"""nnnnnn"""
from decimal import Decimal,getcontext,ROUND_DOWN
getcontext().prec = 100000
n = Decimal(input())
k = int(input())
for _ in range(k):
    increase = n * Decimal("0.0381")
    increase = increase.quantize(Decimal("0.01"),rounding=ROUND_DOWN)
    n = n + increase
print(n.quantize(Decimal("0.01")))
