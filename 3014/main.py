"""nnn"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())
x = d // a
y = x
if not b :
    print(x)
else:
    while y >= b:
        x +=c
        y -=b
        y +=c
    print(x)

# x = 0
# i = 1
# if not b:
#     print(a*d)
# else:
#     while d >= a :
#         if not i % b and d >= a:
#             i =0
#             x +=c

#         else:
#             if d >= a:
#                 d -=a
#                 x +=1
#                 i +=1

# print(x)
