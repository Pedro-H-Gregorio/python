def ehPrimo(number):
      if number % 2 == 0:
            return True
      else:  
            return False
      
while True:
   n = int(input())
   if n<0:
      break
   print(ehPrimo(n)and 'É par' or 'Não é par')