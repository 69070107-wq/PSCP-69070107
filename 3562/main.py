"""nnnnnn"""
x = input()
cha = 0
chaup = 0
num = 0

for i in x :
    if i.isdigit():
        num +=1
    elif i.isupper():
        chaup +=1
    elif i.islower():
        cha +=1
print(f"{chaup} {cha} {num}")
