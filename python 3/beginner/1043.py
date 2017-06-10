a, b, c= [float(i) for i in input().split()]

if (a < (b + c) and b < (a + c) and c < (a + b)):
    print("Perimetro = {0:.1f}".format(a + b + c))
else:
    print("Area = {0:.1f}".format(((a + b) * c) / 2))
