"""nnnnn"""
import math
r, x, y= map(int, input().split())

cssss = math.sqrt((x**2) + (y **2))
if cssss < r :
    print("IN")
elif cssss == r :
    print("ON")
elif cssss > r :
    print("OUT")
