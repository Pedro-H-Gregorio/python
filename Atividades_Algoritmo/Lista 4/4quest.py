reais = int(input())
cedulas = [50,10]
notas = [0,0]
for i in range(len(notas)):
    while reais >= cedulas[i]:
        reais -= cedulas[i]
        notas[i] += 1
print("O minimo de ntoas que ele pode entregar é:",
      f"{notas[0]} notas de {cedulas[0]} reais",
      f"{notas[1]} notas de {cedulas[1]} reais",
      sep="\n")