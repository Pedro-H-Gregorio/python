n = list(map(float,input().split(" ")))

print("TRIANGULO: %.3f"%(n[0]*n[2]/2))
print("CIRCULO: %.3f"%(3.14159*(n[2]**2)))
print("TRAPEZIO: %.3f"%((n[0]+n[1])*n[2]/2))
print("QUADRADO: %.3f"%(n[1]**2))
print("RETANGULO: %.3f"%(n[0]*n[1]))