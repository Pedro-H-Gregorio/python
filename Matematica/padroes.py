'''Funções'''
def primeiroGrau(y1,y2):
    b = y1
    a = y2 - b
    return [a,b]

def segundoGrau(y1,y2,y3):
   c = y1
   a ,b = primeiroGrau(y2-c,(y3-c)/2)
   return [a,b,c]

def terceiroGrau(y1,y2,y3,y4):
  d = y1
  a,b,c = segundoGrau(y2-d,(y3-d)/2, (y4-d)/3)
  return [a,b,c,d]


import sys

lista =  list(map(int,sys.argv[1].split(" ")))
funcao = []
controle = []

if len(controle) == 0:
  valoresAB= primeiroGrau(lista[0],lista[1])
  saoIguais = False
  for i in range(len(lista)):
    saoIguais = valoresAB[0]*(i) + valoresAB[1] == lista[i]
  if saoIguais:
    funcao = valoresAB
  else: controle.append(0)
if len(controle) == 1:
  valoresABC = segundoGrau(lista[0], lista[1], lista[2])
  saoIguais = False
  for i in range(len(lista)):
      saoIguais = valoresABC[0]*((i)**2)+valoresABC[1]*(i+1) + valoresABC[2] == lista[i]
  if saoIguais:
    funcao = valoresABC
  else: controle.append(0)
if len(controle) == 2:
  valoresABCD = terceiroGrau(lista[0], lista[1], lista[2], lista[3])
  saoIguais = False
  for i in range(len(lista)):
    saoIguais = valoresABCD[0]*((i)**3) + valoresABCD[1]*((i+1)**2) + valoresABCD[2]*(i+1) + valoresABCD[3] == lista[i]
  if saoIguais:
    funcao = valoresABCD
  else: controle.append(0)

if len(funcao) == 2:
  print(f'f(x)= ({funcao[0]})x + ({funcao[1]})')
elif len(funcao) == 3:
  print(f'f(x)= ({funcao[0]})x² + ({funcao[1]})x + ({funcao[2]})')
elif len(funcao) == 4:
  print(f'f(x)= ({funcao[0]})x³+ ({funcao[1]})x² + ({funcao[2]})x + ({funcao[3]})')
else: print(controle)
   