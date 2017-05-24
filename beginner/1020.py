v = int(input())

y = v // 365
v = v - (y * 365)

m = v // 30
v = v - (m * 30)

d = v

print("{0} ano(s)" .format(y))
print("{0} mes(es)".format(m))
print("{0} dia(s)" .format(d))
