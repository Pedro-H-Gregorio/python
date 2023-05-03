import re
text = input()
regex_replace = r'<([^>]*?)(abc)+(.*?)>'
regex_sub = r'<\1ZZZ\3>'

print(re.match(regex_replace,text))

print(re.sub(r'<([^>]*?)(abc)+(.*?)>',r'<\1ZZZ\3>',text))