import re
palavra = input()
controles = ['B','C','D']
for i in controles:
    print(len(re.findall(rf'[{i}]',palavra)),"Ocorrencias com a letra",i)
