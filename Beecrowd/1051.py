salario = float(input())
renda = [0,2000,3000,4500]
porcentagens = [0,8,18,28]
valoresfixos = [0,0,80,270]
valor = 0

def calculoImposto(salario, index):
    return salario*porcentagens[index]/100

for i in range(len(renda)):
    try:
        if salario > renda[i] and salario <= renda[i+1]:
            valor = calculoImposto(salario-renda[i],i) + valoresfixos[i]
    except:
        if salario > renda[i]:
            valor = calculoImposto(salario-renda[i],i) + valoresfixos[i] + valoresfixos[i-1]

if valor!=0:
    print(f'R$ {valor:.2f}')
else: print("Isento")