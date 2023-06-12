def soma(n):
    return sum(n)

def ehPrimo(number):
    for i in range(2,number):
      if number % i == 0:
          return False
         
    return True

num = []

i = 2
while len(num) < 100:
    if ehPrimo(i):
        num.append(i)
    i+=1
print(*num,f'A soma de todos os 100 primos é :{soma(num)}',sep="\n")