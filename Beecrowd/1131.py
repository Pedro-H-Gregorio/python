golGremio = 0
golInter = 0
empates = 0
while True:
    gols = list(map(int,input().split()))
    print("Novo grenal (1-sim 2-nao)")
    number = input()
    if gols[0]>gols[1]:
        golInter+=1
    elif gols[0]<gols[1]:
        golGremio+=1
    else: empates+=1
    if number == '2':
        break

print(f'{sum([golGremio,golInter,empates])} grenais')
print(f'Inter:{golInter}')
print(f'Gremio:{golGremio}')
print(f'Empates:{empates}')
print(golInter>golGremio and 'Inter venceu mais' or 'Gremio venceu mais')