medias = []
for i in range(2):
    notas = list(map(float,input().split()))
    medias.append(sum(notas)/len(notas))

medias.append(sum(medias)/len(medias))
[print("%.2f" % x) for x in medias if x != medias[-1]]
print("Média da turma %.2f" % medias[-1])