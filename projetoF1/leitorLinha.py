import re
from urllib import request
from criarArquivos import criarArquivo

def leitorLinha(ano):
    html = open(f'./html/races{ano}.html',"r")

    encontrou = False

    for linha in html:
        url = ""

        #Encontrar tbody
        if linha.find('<select class="resultsarchive-filter-form-select" name="meetingKey">') != -1:
            encontrou = True
            continue

        if encontrou:
            if linha.find('</select>') != -1:
                break
            result = re.search(r'\w*/\w*',linha)
            if(result != None and result.group() != "/option"):
                url = f'https://www.formula1.com/en/results.html/{ano}/races/{result.group()}/race-result.html'
                response = request.urlopen(url)
                raceHTML = response.read().decode('UTF-8')
                nomeArquivo = result.group().split('/')
                gp = open(f'./html/{nomeArquivo[1]}.html','w')
                gp.write(raceHTML)
                gp.close()
                criarArquivo(nomeArquivo[1],ano)

    html.close()

        

        