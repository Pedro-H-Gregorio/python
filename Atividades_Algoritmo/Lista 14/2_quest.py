def multiplicacaoEscalar(matriz1, escalar):
  matrizNova = []
  for i in matriz1:
    listaNova = []

    for j in i:
      listaNova.append(j * escalar)

    matrizNova.append(listaNova)
  return matrizNova



ordem = input("Qual a ordem da matriz que deseja inserir? (lxc)").split("x")
matriz = []
for i in range(int(ordem.pop(0))):
    linha = input("Qual a "+str(i+1)+"° linha? ").split(" ")
    mapLista = list(map(int,linha))
    matriz.append(mapLista)

escalar = int(input("Qual o numero escalar que deseja inserir? "))

print(multiplicacaoEscalar(matriz, escalar))
