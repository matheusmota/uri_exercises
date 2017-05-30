import sys

for line in sys.stdin:
    v1, v2 = [int(i) for i in line.split()]
    print(v1 ^ v2)
