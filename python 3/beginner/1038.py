i, t = [int(i) for i in input().split()]

prices = [4.0, 4.5,  5.0, 2.0, 1.5]
print("Total: R$ {0:.2f}".format(prices[i-1]*t))
