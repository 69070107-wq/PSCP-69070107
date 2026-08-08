"""nnnnnnnn"""
num = int(input())
test = ["A","E","I","O","U"]
box = []
vowel = 0
for i in range(num):
    i +=1
    box.append(input())
for j in box :
    if j in test :
        vowel+=1
print(vowel)
