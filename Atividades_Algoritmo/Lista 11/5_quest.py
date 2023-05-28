from functools import reduce
def fatorial(number):
    return reduce(lambda x,y: x*y,sorted(range(1,number+1),reverse=True),1)

while True:
    n = int(input())
    if n<0:
      break
    print(fatorial(n))