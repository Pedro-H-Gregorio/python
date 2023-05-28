def ehPrimo(number):
    for i in range(2,number):
      if number % i == 0:
          return False
         
    return True
      
while True:
   n = int(input())
   if n<0:
      break
   print(ehPrimo(n)and 'É primo' or 'Não é primo')