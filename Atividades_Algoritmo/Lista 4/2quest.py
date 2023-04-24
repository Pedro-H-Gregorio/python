try:
    lista = []
    for i in range(3):
        lista.append(int(input()))
        if lista[0] == 0:
            raise ValueError("Valor 'a' não pode ser 0")
    delta = lista[1]**2 - 4*lista[0]*lista[2]
    if delta < 0:
        raise ValueError("Valor de delta é negativo, então não possui raises")
    elif delta == 0:
        print("X só vai possuir uma raiz",f"X = {-lista[1]/2*lista[0]}",sep="\n")
    else: 
        print("X vai possuir duas raizes",
              f"X¹ = {(-lista[1]+(delta**(1/2)))/2*lista[0]}",
              f"X² = {(-lista[1]-(delta**(1/2)))/2*lista[0]}",sep="\n")

except ValueError as errorValue:
    print(errorValue.args)