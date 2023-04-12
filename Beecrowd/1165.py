cont = int(input)

for i in range(cont):
    number = int(input())
    divisores = []

    for i in range(number+1):
        if i != 0:
            if number%i == 0:
                divisores.append(i)

    if len(divisores) == 2:
        print(f"{number} eh primo")
    else: print(f"{number} nao eh primo")