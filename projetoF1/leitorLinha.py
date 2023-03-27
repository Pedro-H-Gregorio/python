""" with open("race-result.html", "r+", encoding="utf-8") as file:
    arquivo = file.readlines()

for i in arquivo:
    print(arquivo) """

import re

regex = re.compile("span")

encontrouTBody = False

arquivo = open('race-result.html', 'r', encoding="utf-8")
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
            print(regex.sub(linha.strip(),""))
            
            
    
    
arquivo.close()