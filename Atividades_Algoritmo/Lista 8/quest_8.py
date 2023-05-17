palavra = input()[::-1]
controles = ['A','C','G','T']
nova_palavra = ""
for letra in palavra:
    index = controles.index(letra)
    nova_palavra += controles[-1-index]

print(nova_palavra)