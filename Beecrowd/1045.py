n1, n2, n3 = sorted(list(map(float, input().split())),reverse = True)

def classificacao_triangulo(a, b, c):
    a, b, c = map(lambda x: x**2,[a,b,c])
    
    if a == b+c:
        return print("TRIANGULO RETANGULO")
    elif a < b+c:
        return print("TRIANGULO ACUTANGULO")
    elif a > b+c:
        return print("TRIANGULO OBTUSANGULO")

if n1 == n2 and n2 == n3:
    classificacao_triangulo(n1,n2,n3)
    print("TRIANGULO EQUILATERO")
elif n1 == n2 or n2 == n3 or n1 == n3:
    classificacao_triangulo(n1,n2,n3)
    print("TRIANGULO ISOSCELES")
elif n1 >= (n2 + n3):
    print("NAO FORMA TRIANGULO")
else:
    classificacao_triangulo(n1,n2,n3)