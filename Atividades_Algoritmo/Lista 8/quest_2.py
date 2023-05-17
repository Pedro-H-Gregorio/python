import re
palavra = input()
controles = ['a','e','i','o','u']
for i in controles:
    print(len(re.findall(rf'(?i)[{i}]',palavra)),"Ocorrencias com a letra",i)