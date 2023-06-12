def soma(n):
    return sum(n)

s = int(input())
inferior = int(input())
quadrado = [i**2 for i in range(inferior,s+1)]
quadrado.append(soma(quadrado))
[print(i) for i in quadrado if i != quadrado[-1]]
print("A soma de todos é: %.2f" % quadrado[-1])
