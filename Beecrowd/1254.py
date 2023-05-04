import re
controle = True

while controle:
    try:
        replace = 'aBc'
        substituinte = '923'
        text = '<dont replacethis>abcabc<abcabcde>'
        regex_replace = rf'(?i)<([^>]*?)({replace})+(.*?)>'
        regex_sub = r'<\1$$$$$$$$$$$$$$$$\3>'
        old_text = ''
        while re.match(regex_replace,text):
            text = re.sub(regex_replace,regex_sub,text,1).replace('$$$$$$$$$$$$$$$$',substituinte)
        print(text)
    except EOFError:
        break
