import re
from functools import reduce

encontrouTBody = False

arquivo = open('race-result.html', 'r', encoding="utf-8")
texto = ""

for linha in arquivo:
    
    #Encontrar tbody
    if not encontrouTBody and linha.find("tbody") != -1:
        encontrouTBody = True
        continue
    if encontrouTBody:
        if linha.find("tbody") != -1:
            break
        
        #Encontrar nomes e pontos
        if linha.find('class="hide-for-mobile"') != -1 or linha.find('class="bold"') != -1:
            texto += re.sub(r'<.+?>',"",linha.strip()) + " "
    
texto = re.findall(r'[a-zA-Z].\s\w*\s\d{1,2}|\w*\s\d{1,2}',texto)

for i in texto:
    lista = i.split(" ")
    if len(lista) == 3:
        lista = [lista[0]+" "+lista[1],lista[2]]
    novoArquivo = open(f'{lista[0]}.txt','a') 
    novoArquivo.write(f'Ponto: {lista[1]}')
    novoArquivo.close()

arquivo.close()