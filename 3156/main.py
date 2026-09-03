"""nnnnnnn"""
text = input()
num = int(input())
result = ""
for ch in text :
    result += chr((ord(ch) - ord("a") + num) % 26 + ord("a"))
print(result)
