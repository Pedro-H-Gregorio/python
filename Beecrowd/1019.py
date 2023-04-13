n1 = int(input().split())
segundos = 0
minutos = 0
horas = 0

while n1>=0:
    if n1/60 > 0:
        minutos+=1
        n1-=n1/60
