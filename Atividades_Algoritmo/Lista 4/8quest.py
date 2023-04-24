operacao = input("Operacao que deseja fazer : (soma, subtração, multiplicação, divisão)")
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