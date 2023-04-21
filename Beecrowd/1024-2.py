repeticoes = int(input())
senhas = []

for i in range(repeticoes):
    senha = input()[::-1]
    novasenha = ''
    for j in range(len(senha)):
        if j < len(senha)//2:
            num = ord(senha[j])
            if (num >= 65 and num<=90) or (num>=97 and num<=122):
                novasenha += chr(num+3)
            else: novasenha += senha[j]
        elif j >= len(senha)//2: 
            num = ord(senha[j])
            if (num >= 65 and num<=90) or (num>=97 and num<=122):
                novasenha += chr(num+2) 

    senhas.append(novasenha)

for i in senhas:
    print(i)