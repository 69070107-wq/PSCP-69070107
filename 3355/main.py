"""nnnnn"""
num = int(input())
start = num
last = num
result = []

while num != -1:
    num = int(input())

    if num == -1:
        if start == last:
            result.append(str(start))
        else:
            result.append(str(start) + "-" + str(last))
    elif num == last + 1:
        last = num
    else:
        if start == last:
            result.append(str(start))
        else:
            result.append(str(start) + "-" + str(last))
        start = num
        last = num

print(", ".join(result))
