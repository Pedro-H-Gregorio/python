#! /usr/bin/python3

# FUNÇÕES UTILIZADAS

def divisor(quebra):
  return print("-------------------------------------------------------------"+quebra);

def confirmacao(input):
  if input== "S" or input == "s":
    return True
  else: return False

def multiplicacaoEscalar(matriz1, escalar):
  matrizNova = []
  for i in matriz1:
    listaNova = []

    for j in i:
      listaNova.append(j * escalar)

    matrizNova.append(listaNova)
  return matrizNova

def operacacaoComMatriz(matriz1, matriz2, operacao):
  matrizNova = []
  contadorColuna = 0
  contadorLinha = 0

  for i in matriz1:
    listaNova = []
    
    for j in i:
      match operacao:
        case "*":
          listaNova.append(j * matriz2[contadorColuna][contadorLinha])
        case "+":
          listaNova.append(j + matriz2[contadorLinha][contadorColuna])
        case "-":
          listaNova.append(j - matriz2[contadorLinha][contadorColuna])
        case "and":
          listaNova.append(min([j,matriz2[contadorLinha][contadorColuna]]))
        case "or":
          listaNova.append(max([j,matriz2[contadorLinha][contadorColuna]]))
        case "*and":
          listaNova.append(min([j,matriz2[contadorColuna][contadorLinha]]))

      contadorColuna += 1
    
    matrizNova.append(listaNova)
    contadorLinha += 1
    contadorColuna = 0
  
  return matrizNova

def operacaoGeral(operacao1, matriz1, escalar1, matriz2):
  if escalar1 != "":
    return multiplicacaoEscalar(matriz1, escalar1)
  else: 
    return operacacaoComMatriz(matriz1, matriz2, operacao1)
     
# EXECUÇÃO DO CÓDIGO
            
divisor("")
print("MATRIZES")
divisor("\n")

matrizes = []
controle = [True, False]
operacao = []
escalar = []
resultados = []

while controle[0]:
  divisor("")
  ordem = input("Qual a ordem da "+str(len(matrizes)+1)+"° matriz que deseja inserir? ").split("x")
  matriz = []

  for i in range(int(ordem.pop(0))):
    linha = input("Qual a "+str(i+1)+"° linha? ").split(" ")
    mapLista = list(map(lambda el: int(el),linha))
    matriz.append(mapLista)
  matrizes.append(matriz)

  confirmar = input("Deseja fazer adiconar mais uma matriz ? (S/N) ")
  controle[0] = confirmacao(confirmar)

  if controle[0] == False:
    escalarConfirmar = input("Deseja adicionar um número escalar? (S/N) ")
    controle[1] = confirmacao(escalarConfirmar)

  if controle[1]: 
    valorEscalar = float(input("Qual o valor? "))
    escalar.append(valorEscalar)
  else: 
    escalar.append("")
  
  if controle[0] and controle[1]:
    operacao.append("*")
    operacao.append(input("Qual operação quer fazer ? (+|-|*|and|or|*and) "))
  elif not controle[0] and controle[1]:
    operacao.append("*")
  elif controle[0] and not controle[1]: 
    operacao.append(input("Qual operação quer fazer ? (+|-|*|and|or|*and) "))


for i in range(len(operacao)):
  matrizSecundaria = 0
  matrizPrimaria = 0
  
  if len(resultados) == 0:
    matrizPrimaria = matrizes[i]
  else:
    matrizPrimaria = resultados[i-1]  

  try:
    matrizSecundaria = matrizes[i+1]
  except: 
    if matrizPrimaria == matrizes[i]:
      matrizSecundaria = 0
    else: matrizSecundaria = matrizes[i]
  
  resultados.append(operacaoGeral(operacao[i],matrizPrimaria,escalar[i], matrizSecundaria))

divisor("")
resultadoFinal = resultados.pop()
print(resultadoFinal)