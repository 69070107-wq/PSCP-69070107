"""nnnnn"""
a = int(input())
b = int(input())
goal = int(input())
# small = 0
# while goal > 0:
#     if b > 0 and goal > 5 :
#         goal -=5
#         b-=1
#     elif a > 0 :
#         goal-=1
#         a-=1
#         small+=1
#     else:
#         break
# if not goal :
#     print("-1")
# else:
#     print(small)
big = min(b,goal//5)
goal -= big*5
if goal <= a:
    print(goal)
else:
    print(-1)
