n1, n2, n3, n4 = [float(i) for i in input().split()]

media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1) ) / 10
print("Media: {0:.1f}".format(media))

if(media >= 7):
    print("Aluno aprovado.")
else:
    if(media < 5):
        print("Aluno reprovado.")
    else:
        print("Aluno em exame.")
        nExame = float(input())
        print("Nota do exame: {0:.1f}".format(nExame))
        
        mediaFinal = (media + nExame) / 2
        
        if(mediaFinal  >= 5):
            print("Aluno aprovado.")
        else:
            print("Aluno reprovado.")
        
        print("Media final: {0:.1f}".format(mediaFinal))
