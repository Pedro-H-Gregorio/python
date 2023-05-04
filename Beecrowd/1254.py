import re
controle = True
saida = []
while controle:
    try:
        replace, substituinte, text = map(input,["","",""])

        regex_replace = rf'(?i)<([^>]*?)({replace})(.*?)>'
        regex_sub = r'<\1$$$$$$$$$$$$$$$$\3>'

        while re.search(regex_replace,text) != None:
            text = re.sub(regex_replace,regex_sub,text,1).replace('$$$$$$$$$$$$$$$$',substituinte)
        saida.append(text)
    except EOFError:
        break
print("\n".join(saida))