s = input().split(" ")
n1 = int(s[1])
p1 = float(s[2])

s = input().split(" ")
n2 = int(s[1])
p2 = float(s[2])


t = n1 * p1 + n2 * p2

print("VALOR A PAGAR: R$ %.2f" % t)
