valor1 = float(input("Escreva o primeiro valor :"))
valor2 = float(input("Escreva o segundo valor :"))

operacao = input("Operacao que deseja fazer :")

#operação com if
# if operacao == "+" :
#     print(valor1 + valor2)
# else: 
#    if operacao == "-":
#        print(valor1 - valor2)
#    else: 
#       if operacao == "*":
#           print(valor1 * valor2)
#       else: 
#           if operacao == "/":
#               print(valor1 / valor2)

#operação com match case
# match operacao:
#     case "+":
#         print(valor1+valor2)
#     case "-":
#         print(valor1-valor2)
#     case "*":
#         print(valor1*valor2)
#     case "/":
#         print(valor1/valor2)

#operação com o swtich case
def switch(operacao):
    if operacao == "+":
        return valor2+valor1
    elif operacao == "-":
        return valor1 - valor2
    elif operacao == "*":
        return valor1*valor2
    elif operacao == "/":
        return valor1 / valor2

print(switch(operacao))