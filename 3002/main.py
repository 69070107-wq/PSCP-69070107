name = input()
lastname = input()
age = input()

if len(name) >=5 and len(lastname) >= 5 :
    print(name[0] + name[1] + lastname[-1] + age[-1])
else:
    print(name[0] + age + lastname[-1])