"""Pad Thai"""
food = set()
taste = set()

while True:
    a = input()
    if a == "Cook":
        break
    food.add(a)

while True:
    a = input()
    if a == "End":
        break
    taste.add(a)

want_food = {
    "Pad Thai Sauce", "Tofu", "Pickle Turnip", "Shrimp",
    "Bean Sprouts", "Noodle", "Chives", "Lime",
    "Egg", "Oil", "Peanuts"
}

want_taste = {"Sweet", "Sour", "Salty"}

if food != want_food:
    if food - want_food:
        print("This is not Pad Thai!!!")
    else:
        print("This is bad!")
elif taste == want_taste:
    print("Delicious!")
else:
    print("Not Bad...")
