'''Funções'''
def primeiroGrau(y1,y2):
    b = (2*y1)-y2
    a = y1 - b
    return [a,b]

def segundoGrau(y1,y2,y3):
   c = y3-3*y2+3*y1
   a ,b = primeiroGrau(y1-c,(y2-c)/2)
   return [a,b,c]


import sys

lista =  list(map(int,sys.argv[1].split(" ")))
funcao = None
controle = []

if len(controle) == 0:
  valoresAB= primeiroGrau(lista[0],lista[1])
  saoIguais = False
  for i in range(len(lista)):
    saoIguais = valoresAB[0]*(i+1) + valoresAB[1] == lista[i]
  if saoIguais:
    funcao = valoresAB
  else: controle.append(0)
if len(controle) == 1:
  valoresABC = segundoGrau(lista[0], lista[1], lista[2])
  saoIguais = False
  for i in range(len(lista)):
      saoIguais = valoresABC[0]*((i+1)**2)+valoresABC[1]*(i+1) + valoresABC[2] == lista[i]
      if saoIguais:
        funcao = valoresABC
      else: controle.append(0)

if len(funcao) == 2:
  print(f'f(x)= ({funcao[0]})x + ({funcao[1]})')
elif len(funcao) == 3:
  print(f'f(x)= ({funcao[0]})x² + ({funcao[1]})x + ({funcao[2]})')