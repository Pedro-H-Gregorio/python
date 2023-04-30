n1, n2, n3, n4 = map(float, input().split())
media = (n1 * 2 + n2 * 3 + n3 *4 + n4 * 1)/10
print('Media: %.1f' % media)

if media >= 7:
    print("Aluno aprovado.")
elif media >= 5 and media <= 6.9:
    print("Aluno em exame.")
    exame = float(input())
    print("Nota do exame: %.1f" % exame)
    media_final = (exame + media)/2
    if media_final >= 5:
        print("Aluno aprovado.")
    elif media_final <=4.9:
        print("Aluno reprovado.")
    print("Media final: %.1f" % media_final)
elif media < 5:
    print("Aluno reprovado.")
