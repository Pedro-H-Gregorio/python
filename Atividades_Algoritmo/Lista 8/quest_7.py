import re
palavra = input()
controles = ['D','E','V']
tab = [0,1,3]
pontos = 0
for i,controle in enumerate(controles):
    pontos += len(re.findall(rf'[{controle}]',palavra))*tab[i]

print(pontos)
