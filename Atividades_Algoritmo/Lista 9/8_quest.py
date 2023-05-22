numbers = []

for number in range(300,500):
    ehTriangular = False

    for i in range(number+1):
        if i*(i+1)*(i+2) == number:
            ehTriangular = True
            break

    if ehTriangular: numbers.append(number)

print(" ".join(map(str,numbers)))