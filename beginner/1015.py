import math
x1, y1 = [float(i) for i in input().split()]
x2, y2 = [float(i) for i in input().split()]

print("%.4f" % (math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))))
