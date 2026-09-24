"""nnnnnn"""
tiket = int(input())
while True:
    if tiket <= 0 :
        break
    try:
        age,want_tiket = map(int, input().split())
    except EOFError:
        break
    money = 150 * want_tiket

    if age < 15:
        print("-1")
        continue
    if tiket < want_tiket :
        print("-2")
        continue
    if age <= 22:
        tiket -= want_tiket
        money = money-(money*0.2)
        print(f"{int(money)} {tiket}")
    elif age >= 60 :
        tiket -= want_tiket
        money = money-(money*0.5)
        print(f"{int(money)} {tiket}")
    else:
        tiket -= want_tiket
        print(f"{int(money)} {tiket}")
