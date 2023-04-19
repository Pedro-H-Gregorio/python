n1 = int(input())
const = [365,30]
idade = [0,0]

for i in range(len(idade)):
    while n1 - const[i] >= 0:
        n1 -=const[i]
        idade[i] += 1
idade.append(n1)
print(f"{idade[0]} ano (s)\n{idade[1]} mes(es)\n{idade[2]} dia(s)")