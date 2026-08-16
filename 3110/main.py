"""nnnnn"""
start,end = input().split()
weight = float(input())
price = 0

if start == 'BKK':
    if end == 'CNX':
        price +=(30*weight)
        price +=10
        print(f"{price:.2f}")
    elif end == 'PKT':
        price +=(50*weight)
        price +=25
        print(f"{price:.2f}")
    else:print("Error")
elif start == 'CNX':
    if end == 'UBP':
        price +=(40*weight)
        price +=15
        print(f"{price:.2f}")
    else:print("Error")
elif start == 'UBP':
    if end == 'BKK':
        price +=(40*weight)
        price +=20
        print(f"{price:.2f}")
    elif end == 'PKT':
        price +=(70*weight)
        price +=40
        print(f"{price:.2f}")
    else:print("Error")
elif start == 'PKT':
    if end == 'CNX':
        price +=(60*weight)
        price +=30
        print(f"{price:.2f}")
    else:print("Error")
else:print("Error")
