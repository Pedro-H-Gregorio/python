'''Funções'''
def primeiroGrau(y1,y2):
    b = (2*y1)-y2
    a = y1 - b
    return [a,b]

def segundoGrau(y1,y2,y3):
   c = y3-3*y2+3*y1
   a ,b = primeiroGrau(y1-c,(y2-c)/2)
   return [a,b,c]

def terceiroGrau(y1,y2,y3,y4):
  d = -y4 + 4*y3 - 6*y2 + 4*y1
  a,b,c = segundoGrau(y1-d,(y2-d)/2, (y3-d)/3)
  return [a,b,c,d]


import sys

lista =  list(map(int,sys.argv[1].split(" ")))
funcao = []
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
if len(controle) == 2:
  valoresABCD = terceiroGrau(lista[0], lista[1], lista[2], lista[3])
  saoIguais = False
  for i in range(len(lista)):
    saoIguais = valoresABCD[0]*((i+1)**3) + valoresABCD[1]*((i+1)**2) + valoresABCD[2]*(i+1) + valoresABCD[3] == lista[i]
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
   