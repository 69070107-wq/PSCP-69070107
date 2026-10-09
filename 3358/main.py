"""nnnnnn"""
x = int(input())
num1 = list(map(int, input().split()))
ans = []
for i in range(0,x*2,2):
    ans.append(max(num1[i], num1[i+1]))
if x == 1:
    print(ans[0])
else:
    print(" + ".join(map(str, ans)), "=", sum(ans))
