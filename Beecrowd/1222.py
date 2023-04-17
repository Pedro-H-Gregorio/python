import math
while True:
    try :
        n_palavras, n_linhas, n_caracter = map(int, input().split())
        text = input()
        cont = 0

        palavras = text.split(" ")
        contFrase = 0
        frase = [palavras[cont]]

        while n_palavras-1 != 0:
            cont += 1
            frase[contFrase] += f" {palavras[cont]}"
            n_palavras -= 1
            if len(frase[contFrase]) > n_caracter:
                frase[contFrase] = frase[contFrase][:-(len(palavras[cont]))]
                frase.append(palavras[cont])
                contFrase += 1
        
        print(math.ceil(len(frase)/n_linhas))

    except EOFError:
        break