n = input()
numero = int(n)
notas = [100,50,20,10,5,2,1]
notasTotal = [0,0,0,0,0,0,0]

for i in range(len(notas)):
    while numero >= notas[i]:
        numero -= notas[i]
        notasTotal[i] += 1
print(f"{n}\n{notasTotal[0]} nota(s) de R$ 100,00\n{notasTotal[1]} nota(s) de R$ 50,00\n{notasTotal[2]} nota(s) de R$ 20,00\n{notasTotal[3]} nota(s) de R$ 10,00\n{notasTotal[4]} nota(s) de R$ 5,00\n{notasTotal[5]} nota(s) de R$ 2,00\n{notasTotal[6]} nota(s) de R$ 1,00")