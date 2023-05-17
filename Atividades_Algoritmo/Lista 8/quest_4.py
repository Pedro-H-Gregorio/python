media_anual_turma=0

for i in range(40):
    media_anual_aluno = sum(map(float,input().split()))/4
    print(media_anual_aluno,"de media do aluno")
    media_anual_turma += media_anual_aluno*(1/40)

print(media_anual_turma,"de media da turma")