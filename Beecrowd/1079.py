number = int(input())
for i  in range(number):
    notas = list(map(float,input().split()))
    print(f'{((notas[0]*2)+(notas[1]*3)+(notas[2]*5))/10:.1f}')
