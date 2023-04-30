salario = float(input())
salarioReajuste = [0,400,800,1200,2000]
porcentagens = [15,12,10,7,4]

def prints(salario, porcentagem):
    print(f"Novo salario: {(salario+(salario*porcentagem/100)):.2f}")
    print(f"Reajuste ganho: {(salario*porcentagem/100):.2f}")
    print(f"Em percentual: {porcentagem} %")

    

for i in range(len(salarioReajuste)):
    try:
        if salario > salarioReajuste[i] and salario <= salarioReajuste[i+1]:
            prints(salario,porcentagens[i])
    except:
        if salario > salarioReajuste[i]:
            prints(salario, porcentagens[i])
