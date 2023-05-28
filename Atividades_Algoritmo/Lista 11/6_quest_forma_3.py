def fibonnati(quantidade):
    sequencia = [1,1]
    if quantidade<=2:
       return sequencia[quantidade-1]
    else:
       for i in range(1,quantidade-1):
          sequencia.append(sequencia[-1]+sequencia[-2])
    return sequencia[quantidade-1]

while True:
    n = int(input())
    if n<0:
      break
    print(fibonnati(n))

"""
A mais eficiente das 3 formas que fiz foi essa. Pois é uma maneira que vai abranger mais posições. Porém não
escolha um numero tão alto, seu pc pode dar tela azul igual ao meu quando testes 500000000
"""