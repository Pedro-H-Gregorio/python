def divisor(quebra):
  return print("-------------------------------------------------------------"+quebra);

def confirmacao(input):
  if input== "S" or input == "s":
    return True
  else: return False

divisor("")
print("MATRIZES")
divisor("\n")

matrizes = []
controle = [True, False]
operacao = []
escalar = ""


while controle[0]:
  divisor("")
  ordem = input("Qual a ordem da "+str(len(matrizes)+1)+"° matriz que deseja inserir? ").split("x")
  matriz = []

  for i in range(int(ordem.pop(-1))):
    linha = input("Qual a "+str(i+1)+"° linha? ").split(", ")
    mapLista = list(map(lambda el: int(el),linha))
    matriz.append(mapLista)
  matrizes.append(matriz)

  confirmar = input("Deseja fazer adiconar mais uma? (S/N) ")
  controle[0] = confirmacao(confirmar)

  escalarConfirmar = input("Deseja Adicionar um número escalar? (S/N) ")
  controle[1] = confirmacao(escalarConfirmar)
  if controle[1]: escalar = float(input("Qual o valor? "))
  
  if controle[0] or controle[1]:
    operacao.append(input("Qual operação quer fazer ? (+\-\*) "))

