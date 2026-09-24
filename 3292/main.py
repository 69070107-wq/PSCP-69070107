"""nnnnnn"""
x = input()
y = int(input())
def r():
    """nnnn"""
    for i in range(y):
        print(" "*(2*i) + "*"*(y-i))
    for i in range(2,y+1):
        print(" "*(2 *  (y-i)) + "*"*i)
# =========================================
def l():
    """nnnnnn"""
    for i in range(y):
        print(" "*(y-i-1) + "*"*(y-i))
    for i in range(2, y+1):
        print(" "*(i-1) + "*"*i)


for j, n in enumerate(x):
    if n == 'L':
        l()
    elif n == 'R':
        r()
    if j != len(x)-1:
        print()
