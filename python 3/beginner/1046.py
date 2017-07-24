start, end = [int(i) for i in input().split()]

total = 0

if start >= end:
    total =  24 - start 
    total += end
else:
    total = end - start
    

print("O JOGO DUROU {0} HORA(S)".format(total))
