from functools import reduce

limite_inferior = int(input())
limite_superior = int(input())

print(reduce(lambda x,b: x+b**2,range(limite_inferior,limite_superior+1),0))