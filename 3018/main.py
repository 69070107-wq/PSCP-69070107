"""nnnn"""
x1, y1, w1, h1 = map(int, input().split())
x2, y2, w2, h2 = map(int, input().split())

overlap_w = min(x1 + w1,x2 + w2) - max(x1,x2)
overlap_h = min(y1 + h1,y2 + h2) - max(y1,y2)

if overlap_h > 0 and overlap_w > 0 :
    print(overlap_w*overlap_h)
else:
    print("no overlapping")