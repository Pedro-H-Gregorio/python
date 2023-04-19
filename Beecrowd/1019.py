n1 = int(input())
const = [3600,60]
tempo = [0,0]

for i in range(len(tempo)):
    while n1 - const[i] >= 0:
        n1 -=const[i]
        tempo[i] += 1
tempo.append(n1)
print(f"{tempo[0]}:{tempo[1]}:{tempo[2]}")