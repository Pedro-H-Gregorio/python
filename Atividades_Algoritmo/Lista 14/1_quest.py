def multiplicacaoMatrizes(matriz1, matriz2):
  matrizNova = []

  for i in range(len(matriz1)):
    linhaNova = []
    
    for j in range(len(matriz2[0])):
      resultado = 0
      
      for k in range(len(matriz2)):
        resultado += matriz1[i][k] * matriz2[k][j]
      
      linhaNova.append(resultado)
    
    matrizNova.append(linhaNova)

  return matrizNova

matrizes = []
ordens = []

try:
    for i in range(2):
        ordem = input("Qual a ordem da "+str(len(matrizes)+1)+"° matriz que deseja inserir? ").split("x")
        ordens.append(ordem)
        matriz = []
        for i in range(int(ordem[0])):
            linha = input("Qual a "+str(i+1)+"° linha? ").split(" ")
            mapLista = list(map(int,linha))
            matriz.append(mapLista)
        matrizes.append(matriz)

    if ordens[0][-1] != ordens[1][0]:
        raise ValueError()

    print(multiplicacaoMatrizes(matrizes[0], matrizes[1]))
except:
   print("Não é possivel fazer a multiplicação")