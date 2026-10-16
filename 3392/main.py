"""nnnnnnn"""

a = [0] * 50

for i in range(3):
    a[i] = int(input())
    print(f"Input number {i + 1} stored.")

while True:
    menu = int(input())

    if menu == 1:
        print("Original order:", *a[:3])
    elif menu == 2:
        print("Descending order:", *sorted(a[:3], reverse=True))
    elif menu == 3:
        print("Ascending order:", *sorted(a[:3]))
    elif not menu:
        break
