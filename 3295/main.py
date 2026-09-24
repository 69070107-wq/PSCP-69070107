"""bnnnnnnnnnnnn"""
x = int(input())
n = 0
if  x <= 10 :
    n = x*5
elif x <= 50 :
    n = 5 * 10 + (x - 10)* 7
elif x <= 100:
    n = 5 * 10 + 40 * 7 + (x - 50) * 10
elif x <= 200:
    n = 5 * 10 + 40 * 7 + 50 * 10 + (x - 100) * 12
else:
    n = 5 * 10 + 40 * 7 + 50 * 10 + 100 * 12 +(x - 200) * 15
satang = n *100
ft = x * 50
vat = n * 7
tt = satang + ft + vat

pp = (tt + 5) //10
bath = pp //10
dec = pp % 10


print(f"{bath}.{dec}")
