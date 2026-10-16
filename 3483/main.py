
"""nnnnnnnn"""
d1 = input().split()
n = int(d1[0])
m = int(d1[1])

if n < 1 or n > 10 or m < 1 or m > 20:
    print("Data Incorrect")
else:
    teams = []
    wrong = False
    i = 0

    while i < n:
        d2 = input().split()
        scores = []
        j = 0

        while j < m:
            x = int(d2[j])
            if x < 0 or x > 100:
                wrong = True
            scores.append(x)
            j += 1

        teams.append(scores)
        i += 1

    if wrong:
        print("Data Incorrect")
    else:
        total = 0
        i = 0

        while i < n:
            s = 0
            mx = 0
            j = 0

            while j < m:
                x = teams[i][j]
                s += x

                if x > mx:
                    mx = x
                j += 1

            avg = s / m
            total += s
            print(f"Team {i + 1}: Average = {avg:.2f}, Max = {mx}")
            i += 1

        print(f"Total Score of All Teams = {total}")
