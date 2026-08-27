"""nnnnnnnnn"""
start = input()
end = input()

sh, sm = map(int, start.split('.'))
eh, em = map(int, end.split('.'))

if sh > 23 or eh > 23 or sm > 59 or em > 59:
    print("ERROR")
else:
    start_min = sh * 60 + sm
    end_min = eh * 60 + em

    if end_min < start_min:
        print("ERROR")
    else:
        minutes = end_min - start_min

        if minutes <= 15:
            print("FREE")
        elif minutes <= 60:
            print(25)
        elif minutes <= 120:
            print(50)
        elif minutes <= 180:
            print(80)
        elif minutes <= 240:
            print(110)
        elif minutes <= 300:
            print(145)
        elif minutes <= 360:
            print(180)
        elif minutes <= 1440:
            print(250)
        else:
            print("ERROR")
