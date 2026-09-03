"""nnnn"""
N, K, T = map(int, input().split())

if T == 1 :
    print(1)
else:
    person = 1
    count = 1

    while True:
        person = (person + K - 1) % N + 1

        if person == T:
            count += 1
            print(count)
            break

        if person == 1:
            print(count)
            break

        count += 1
