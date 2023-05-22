number = int(input())
ehTriangular = False

for i in range(number+1):
    if i*(i+1)*(i+2) == number:
        ehTriangular = True
        break

print(ehTriangular and 'É triangular' or 'Não é triangular')