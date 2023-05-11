cont = 0
for i in range(10):
    cont += int(input())
print(cont)

""" # Outra maneira apenas aprendizado
from functools import reduce
print(reduce(lambda x,b: x+b,list(map(int,input().split())),0)) """