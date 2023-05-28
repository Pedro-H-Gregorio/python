def ehTriangular(number):
    for i in range(number+1):
      if i*(i+1)*(i+2) == number:
        return True
         
    return False
      
while True:
   n = int(input())
   if n<0:
      break
   print(ehTriangular(n) and 'É triangular' or 'Não é triangular')