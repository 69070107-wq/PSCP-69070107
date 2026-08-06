"""nnn"""
word = input().lower()

a = []
e = []
i = []
o = []
u = []
for j in word :
    if j == 'a' :
        a.append(j)
    elif j == 'e' :
        e.append(j)
    elif j == 'i' :
        i.append(j)
    elif j == 'o' :
        o.append(j)
    elif j == 'u' :
        u.append(j)

if a :
    print(f"a : {len(a)}")
if e :
    print(f"e : {len(e)}")
if i :
    print(f"i : {len(i)}")
if o :
    print(f"o : {len(o)}")
if u :
    print(f"u : {len(u)}")
