def determinanteMatriz2(matriz):
    return matriz[0][0]*matriz[1][1] - matriz[1][0]*matriz[0][1]

def calculaPivo(linhaMatriz):
    pivos= []
    for i in range(len(linhaMatriz)):
        pivos.append(linhaMatriz[i]*((-1)**(2+i)))
    return pivos

def parteMatriz(matrizCompleta):
    matrizes = []
    for i in range(len(matrizCompleta)):
        matriz = []
        for j in range(len(matrizCompleta)):
            linhaCorrente = matrizCompleta[j].copy()
            if j == 0:
                continue
            linhaCorrente.pop(i)
            matriz.append(linhaCorrente)
        matrizes.append(matriz)
    return matrizes

def calculaDeterminantesMatriz(matrizCompleta):
    valores = []
    for m in range(len(matrizCompleta)):
        if len(matrizCompleta[m]) == 2:
             valores.append(determinanteMatriz2(matrizCompleta[m]))
             continue
        pivos = calculaPivo(matrizCompleta[m][0])
        determinantes = calculaDeterminantesMatriz(parteMatriz(matrizCompleta[m]))
        v = []
        for i in range(len(pivos)):
            v.append(pivos[i]*determinantes[i])
        valores.append(sum(v))
        
    return valores

try:
    ordem = input("Qual a ordem da matriz que deseja inserir? (lxc)").split("x")
    matriz = []
    for i in range(int(ordem[0])):
        linha = input("Qual a "+str(i+1)+"° linha? ").split(" ")
        mapLista = list(map(int,linha))
        matriz.append(mapLista)
    if ordem[1] != ordem[0]:
        raise ValueError()
    print(*calculaDeterminantesMatriz([matriz]))

except:
   print("Não é possivel fazer a determinante")
