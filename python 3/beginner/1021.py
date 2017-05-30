
v = float(input())

rest = v % 1
v = int((v - rest))
rest = int((rest * 100))

n100 = v // 100
v = v - (100 * n100)

n50 = v // 50
v = v - (50 * n50)

n20 = v // 20
v = v - (20 * n20)


n10 = v // 10
v = v - (10 * n10)

n5 = v // 5
v = v - (5 * n5)

n2 = v // 2
v = v - (2 * n2)


print("NOTAS:")
print("{0} nota(s) de R$ 100.00".format(n100))
print("{0} nota(s) de R$ 50.00" .format(n50))
print("{0} nota(s) de R$ 20.00" .format(n20))
print("{0} nota(s) de R$ 10.00" .format(n10))
print("{0} nota(s) de R$ 5.00"  .format(n5))
print("{0} nota(s) de R$ 2.00"  .format(n2))

m1 = v

m050 = rest // 50
rest = rest - (50 * m050)

m025 = rest // 25
rest = rest - (25 * m025)

m010 = rest // 10
rest = rest - (10 * m010)

m005 = rest // 5
rest = rest - (5 * m005)

m001 = rest 

print("MOEDAS:")
print("{0} moeda(s) de R$ 1.00".format(m1))
print("{0} moeda(s) de R$ 0.50".format(m050))
print("{0} moeda(s) de R$ 0.25".format(m025))
print("{0} moeda(s) de R$ 0.10".format(m010))
print("{0} moeda(s) de R$ 0.05".format(m005))
print("{0} moeda(s) de R$ 0.01".format(m001))


