peso, altura = map(float, input().split())
imc = peso/altura**2
if imc < 20:
    print("Abaixo do peso")
elif imc >= 20 and imc <= 25:
    print("Normal")
elif imc > 25 and imc <= 30:
    print("Excesso de peso")
elif imc > 30 and imc <= 35:
    print("Obesidade")
elif imc > 35 :
    print("Obesidade mórbida")