"""nnnnnnnn"""
year = int(input())
cc = int(input())

if year <= 1990 :
    if cc <= 1500 :
        print("1250")
    elif 2000 >= cc > 1500 :
        print("1400")
    elif cc > 2000 :
        print("2000")
elif 1999 >= year >= 1991 :
    if cc <= 1500 :
        print("1100")
    elif 2000 >= cc > 1500 :
        print("1300")
    elif cc > 2000 :
        print("1700")
elif year >= 2000 :
    if cc <= 1500 :
        print("1000")
    elif 2000 >= cc > 1500 :
        print("1200")
    elif cc > 2000 :
        print("1500")
