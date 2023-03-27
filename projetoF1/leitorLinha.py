""" with open("race-result.html", "r+", encoding="utf-8") as file:
    arquivo = file.readlines()

for i in arquivo:
    print(arquivo) """

arquivo = open('race-result.html', 'r', encoding="utf-8")
for linha in arquivo:
    print(linha.split("\n?\r"))
arquivo.close()