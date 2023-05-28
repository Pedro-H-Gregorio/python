def fibonnati(quantidade):
    if quantidade < 2:
      return quantidade
    else:
      return fibonnati(quantidade - 1) + fibonnati(quantidade -2)

while True:
    n = int(input())
    if n<0:
      break
    print(fibonnati(n))