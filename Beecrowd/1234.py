import re
while True:
    try :
        text = input()
        fraseNova = ""
        for i in text:
            try:
                ultima_letra = re.search(r'\w\s*$', fraseNova).group()
                if ultima_letra.strip() == ultima_letra.strip().upper():
                    fraseNova += i.lower()
                else: fraseNova += i.upper()
            except:
                fraseNova += i.upper()

        print(fraseNova)
    except EOFError:
        break