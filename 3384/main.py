"""nnnnnnnn"""
x = input()[1:-1].split(",")
n = False
for i in x:
    i = int(i)
    if not i % 2 :
        print(i)
        n = True
if not n:
    print("Nope")
