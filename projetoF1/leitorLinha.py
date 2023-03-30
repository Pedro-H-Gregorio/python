import re
from urllib import request
from criarArquivos import criarArquivo

def leitorLinha(html, ano):
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
            result = re.search(r'"\w*/\w*"',linha)
            if(result != None):
                url = f'https://www.formula1.com/en/results.html/{ano}/races/{result.group()}/race-result.html'
                response = request.urlopen(url)
                raceHTML = response.read().decode('UTF-8')
                criarArquivo(raceHTML.split("\n"),ano)

        

        