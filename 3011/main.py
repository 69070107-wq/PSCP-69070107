"""7676"""
x = input()
y = input()

if (x == 'Red' and y == 'Yellow') or (x == 'Yellow' and y == 'Red'):
    print("Orange")
elif (x == 'Red' and y == 'Blue') or (x == 'Blue' and y == 'Red'):
    print("Violet")
elif (x == 'Yellow' and y == 'Blue') or (x == 'Blue' and y == 'Yellow'):
    print("Green")
elif (x == 'Yellow' and y == 'Yellow') :
    print("Yellow")
elif (x == 'Red' and y == 'Red') :
    print("Red")
elif (x == 'Blue' and y == 'Blue') :
    print("Blue")
else:
    print("Error")
