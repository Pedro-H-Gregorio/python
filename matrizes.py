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

def retornaElementosMatriz(matriz, linha, coluna):
  contadorLinha = 0
  contadorColuna = 0

  for i in matriz:
    if contadorLinha == linha:
      for j in i:
        if contadorColuna == coluna:
          return j
        else:
          contadorColuna += 1
    else:
      contadorLinha += 1

def operacacaoComMatriz(matriz1, matriz2, operacao):
  matrizNova = []
  contadorColuna = 0
  contadorLinha = 0

  for i in matriz1:
    listaNova = []
    
    for j in i:
      match operacao:
        case "*":
          elementoMatriz2 = retornaElementosMatriz(matriz2, contadorColuna, contadorLinha)
          listaNova.append(j * elementoMatriz2)
        case "+":
          elementoMatriz2 = retornaElementosMatriz(matriz2, contadorLinha, contadorColuna)
          listaNova.append(j + elementoMatriz2)
        case "-":
          elementoMatriz2 = retornaElementosMatriz(matriz2, contadorLinha, contadorColuna)
          listaNova.append(j - elementoMatriz2)
        case "and":
          elementoMatriz2 = retornaElementosMatriz(matriz2, contadorLinha, contadorColuna)
          listaNova.append(min([j,elementoMatriz2]))
        case "or":
          elementoMatriz2 = retornaElementosMatriz(matriz2, contadorLinha, contadorColuna)
          listaNova.append(max([j,elementoMatriz2]))
        case "*and":
          elementoMatriz2 = retornaElementosMatriz(matriz2, contadorColuna, contadorLinha)
          listaNova.append(min([j,elementoMatriz2]))

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

  for i in range(int(ordem.pop(-1))):
    linha = input("Qual a "+str(i+1)+"° linha? ").split(" ")
    mapLista = list(map(lambda el: int(el),linha))
    matriz.append(mapLista)
  matrizes.append(matriz)

  escalarConfirmar = input("Deseja adicionar um número escalar? (S/N) ")
  controle[1] = confirmacao(escalarConfirmar)

  confirmar = input("Deseja fazer adiconar mais uma matriz ? (S/N) ")
  controle[0] = confirmacao(confirmar)

  if controle[1]: 
    valorEscalar = float(input("Qual o valor? "))
    escalar.append(valorEscalar)
  else: 
    escalar.append("")
  
  if controle[0] and controle[1]:
    operacao.append("*")
    operacao.append(input("Qual operação quer fazer ? (+|-|*|and|or|*and) "))
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