v = int(input())

h = v // 3600
v = v - (h * 3600)

m = v // 60
v = v - (m * 60)

s = v

print("{0}:{1}:{2}".format(h,m,s))

