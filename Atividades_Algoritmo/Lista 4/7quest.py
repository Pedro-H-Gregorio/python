anoComparativo = int(input())
ano = anoComparativo
regras = [400,4]
for i in range(len(regras)):
    while ano >= regras[i]:
        ano -= regras[i]
if ano == 0:
    print(f"{anoComparativo} é ano bissexto")
else: 
    print(f"{anoComparativo} não é ano bissexto")
