import sys
import os
diretorio = sys.argv[1]

for path in os.listdir(diretorio):

    #Recuperaçao de arquivos e leitores
    arquivo = open(diretorio+path,'r')
    valores = arquivo.read().split("\n")
    valores.pop()
    valores = list(map(int,valores))

    for index in range(len(valores)):
        if(index != 0):
            valores[index] += valores[index-1]

    arquivo.close()
    os.remove(diretorio+path)
    novoArquivo = open(diretorio+path, "a")

    for linhas in valores:
        novoArquivo.write(f'{linhas}\n')
    
    novoArquivo.close()