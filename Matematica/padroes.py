'''Funções'''
def primeiroGrau(lista):
    b = (2*lista[0])-lista[1]
    a = lista[0] - b
    return [a,b]

import sys

lista =  list(map(int,sys.argv[1].split(" ")))
funcao = None
temPadrao = False

while not temPadrao:
    controle = []
    if controle == []:
      valoresAB= primeiroGrau(lista)
      saoIguais = False
      for i in range(len(lista)):
        saoIguais = valoresAB[0]*(i+1) + valoresAB[1] == lista[i]
      if saoIguais:
         temPadrao = True
         funcao = valoresAB
      else: controle.append(False)

print(f'f(x)= {funcao[0]}x {funcao[1]}')