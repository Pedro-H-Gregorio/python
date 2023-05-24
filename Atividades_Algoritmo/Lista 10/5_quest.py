string = input()
cont = 0
caracter = ""
for i in string:
    controle = 0
    for j in string:
        if i == j:
            controle+=1
    if controle > cont:
        cont = controle
        caracter = i

print(caracter,cont)