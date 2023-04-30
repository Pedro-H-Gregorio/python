totalPositivos = 0
somatorio = 0

for i in range(6):
    n = float(input())
    if n>0:
        totalPositivos += 1
        somatorio += n

print(f'{totalPositivos} valores positivos')
print(f'{(somatorio/totalPositivos):.1f}')