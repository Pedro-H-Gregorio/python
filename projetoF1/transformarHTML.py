import sys
from urllib import request
from leitorLinha import leitorLinha

# Recuperar argumentos da linha de comando
if len(sys.argv) < 3:
    print('argumentos insuficientes\nO primeiro argumento deve ser a url do site.\nO segundo deve ser o ano da F1')
    sys.exit()

url = sys.argv[1]
ano = sys.argv[2] 

#conectar com a internet para resgatar o html
response = request.urlopen(url)
html = response.read().decode('UTF-8')

leitorLinha(html.split("\n"),ano)