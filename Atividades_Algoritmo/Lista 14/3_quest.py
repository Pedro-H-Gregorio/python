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

def calculaDeterminantesMatriz(matrizCompleta, valores = []):
    for m in matrizCompleta:
        if len(m) == 2:
             valores.append(determinanteMatriz2(m))
             continue
        if len(m) == 3:
            calculaDeterminantesMatriz(parteMatriz(m))
            continue
        valores = resultadoDeterminante(parteMatriz(m))
        
        
    return valores

def resultadoDeterminante(matrizCompleta, resultados = []):
    for m in matrizCompleta:
        pivos = calculaPivo(m[0])
        valoresDeterminantes = calculaDeterminantesMatriz([m])
        resultado = 0
        for i in range(1,len(pivos)+1):
            resultado += pivos[-i]*valoresDeterminantes[-i]
        resultados.append(resultado)
    return resultados

try:
    ordem = input("Qual a ordem da matriz que deseja inserir? ").split("x")
    matriz = []
    for i in range(int(ordem[0])):
        linha = input("Qual a "+str(i+1)+"° linha? ").split(" ")
        mapLista = list(map(int,linha))
        matriz.append(mapLista)
    if ordem[1] != ordem[0]:
        raise ValueError()
    print(resultadoDeterminante([matriz])[-1])

except:
   print("Não é possivel fazer a determinante")
