repeticoes = int(input())
senhas = []

for i in range(repeticoes):
    senha = input()[::-1]
    novasenha = ''
    for j in range(len(senha)):
        num = ord(senha[j])
        letter = ""
        if (num >= 65 and num<=90) or (num>=97 and num<=122):
            letter = chr(num+3)
        else: letter = senha[j]
        if j >= len(senha)//2:
            letter = chr(ord(letter)-1)
        novasenha += letter

    senhas.append(novasenha)

for i in senhas:
    print(i)