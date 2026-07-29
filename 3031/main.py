"""nnnnnn"""
import math
ink,response = map(int, input().split())

for i in range(response):
    i +=i
    positionx,positiony = map(int, input().split())
    d = math.sqrt((positionx**2)+(positiony**2))
    zone = 3.1416*(d**2)
    t = zone / ink
    print(math.ceil(t))
