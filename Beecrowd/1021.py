numero = float(input())
notas = [100,50,20,10,5,2,1,0.50,0.25,0.10,0.05,0.01]
notasTotal = [0,0,0,0,0,0,0,0,0,0,0,0]

for i in range(len(notas)):
    while numero >= notas[i]:
        print(numero)
        numero = round(numero-notas[i],2)
        notasTotal[i] += 1
print(f"NOTAS:\n{notasTotal[0]} nota(s) de R$ 100.00\n{notasTotal[1]} nota(s) de R$ 50.00\n{notasTotal[2]} nota(s) de R$ 20.00\n{notasTotal[3]} nota(s) de R$ 10.00\n{notasTotal[4]} nota(s) de R$ 5.00\n{notasTotal[5]} nota(s) de R$ 2.00")
print(f"MOEDAS:\n{notasTotal[6]} moeda(s) de R$ 1.00\n{notasTotal[7]} moeda(s) de R$ 0.50\n{notasTotal[8]} moeda(s) de R$ 0.25\n{notasTotal[9]} moeda(s) de R$ 0.10\n{notasTotal[10]} moeda(s) de R$ 0.05\n{notasTotal[11]} moeda(s) de R$ 0.01")
