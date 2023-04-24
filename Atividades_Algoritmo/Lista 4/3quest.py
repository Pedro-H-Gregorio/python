n1, n2, n3 = map(float, input().split())
media = (n1 + n2 + n3)/3
if media >= 7:
    print("Aluno aprovado")
elif media >= 4 and media <  7:
    print("Aluno deve fazer prova final")
elif media < 4: print("Aluno reprovado")