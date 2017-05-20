v = int(input())
print(v)

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

n1 = v

print("{0} nota(s) de R$ 100,00".format(n100))
print("{0} nota(s) de R$ 50,00" .format(n50))
print("{0} nota(s) de R$ 20,00" .format(n20))
print("{0} nota(s) de R$ 10,00" .format(n10))
print("{0} nota(s) de R$ 5,00"  .format(n5))
print("{0} nota(s) de R$ 2,00"  .format(n2))
print("{0} nota(s) de R$ 1,00"  .format(n1))
