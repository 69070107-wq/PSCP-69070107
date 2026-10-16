"""nnnnnnn"""

n1 = input()
n2 = input()
k = input()
p = input()

color = {
    "Black": "0", "Brown": "1", "Red": "2",
    "Orange": "3", "Yellow": "4", "Green": "5",
    "Blue": "6", "Purple": "7", "Grey": "8", "White": "9"
}

multi = {
    "Black": 1, "Brown": 10, "Red": 100,
    "Orange": 1000, "Yellow": 10000, "Green": 100000,
    "Blue": 10**6, "Purple": 10**7, "Gold": 0.1, "Silver": 0.01
}

per = {
    "Brown": 1, "Red": 2, "Green": 0.5,
    "Blue": 0.25, "Purple": 0.1, "Grey": 0.05,
    "Gold": 5, "Silver": 10
}

if n1 not in color or n2 not in color or k not in multi or p not in per:
    print("Error")
else:
    num = int(color[n1] + color[n2]) * multi[k]
    low = num * (100 - per[p]) / 100
    high = num * (100 + per[p]) / 100
    print(f"{low:.4f}")
    print(f"{high:.4f}")
