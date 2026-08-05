"""nnnnn"""
year = int(input())

if not year % 400:
    print("yes")
elif not year % 100 and year > 1500:
    print("no")
elif not year % 4:
    print("yes")
else:print("no")
