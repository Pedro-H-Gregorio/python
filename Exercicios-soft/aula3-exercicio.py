def divisor(quebra):
  return print("-------------------------------------------------------------"+quebra)

divisor("")
print("CONVOCAÇÕES PARA O EXÉRCITO BRASILEIRO")
divisor("\n")

divisor("")
nome = input("Escreva seu nome:")
idade = float(input("Escreva sua idade: "))
altura = float(input("Escreva sua altura em metros: "))
peso = float(input("Escreva seu peso: "))
divisor("\n")

print("Senhor(a)",nome+",","você tem:\n",idade,"Anos\n","pesa:",peso,"kg\n",altura,"m de altura.")
divisor("")
print("Verificando qualificações para o exército brasilero...")
divisor("\n")

if(idade >= 18 and peso>=60 and altura>=1.70):
  print("Parabéns senhor(a)",nome,"Está sendo convocado para o exército!")
  divisor("")
else:
  print("Infelizmente, você não é qualificado para o exército")
  divisor("")