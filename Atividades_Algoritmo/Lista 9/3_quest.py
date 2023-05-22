while True:
    print("______ CALCULADORA - MENU______","Operacao que deseja fazer? (soma, subtração, multiplicação, divisão, sair)",sep="\n")
    operacao = input()
    
    if operacao == 'sair':
        break

    valor1 = float(input("Escreva o primeiro valor :"))
    valor2 = float(input("Escreva o segundo valor :"))

    if operacao == "soma" :
        print(valor1 + valor2)
    elif operacao == "subtração":
        print(valor1 - valor2)
    elif operacao == "multiplicação":
        print(valor1 * valor2)
    elif operacao == "divisão":
        print(valor1 / valor2)