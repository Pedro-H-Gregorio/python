totalPositivos = 0

for i in range(6):
    n = float(input())
    if n>0:
        totalPositivos += 1

print(f'{totalPositivos} valores positivos')