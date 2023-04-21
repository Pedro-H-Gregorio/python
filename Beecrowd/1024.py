import re

def mudarCaracterEm3(el):
    try:
        caracter = re.match(r'[A-Za-z]',el).group()
        return chr(ord(caracter)+3)
    except:
        return el
    
def mudarCaracterEm2(el):
    try:
        caracter = re.match(r'[A-Za-z]',el).group()
        return chr(ord(caracter)+2)
    except:
        return el

repeticoes = int(input())

for i in range(repeticoes):
    senha = input()[::-1]
    lista1 = list(map(mudarCaracterEm3,senha[0:len(senha)//2]))
    lista2 = list(map(mudarCaracterEm2,senha[len(senha)//2:]))
    print("".join(lista1+lista2))