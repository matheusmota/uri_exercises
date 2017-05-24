import math 

a, b, c = [float(i) for i in input().split()]

d=(pow(b,2)-(4*a*c))

if(a!=0 and d>0):
    r1 = ( -b + math.sqrt(d) ) / ( 2 * a)
    r2 = ( -b - math.sqrt(d) ) / ( 2 * a)
    
    print("R1 = {0:.5f}".format(r1))
    print("R2 = {0:.5f}".format(r2))
else:
    print("Impossivel calcular")
