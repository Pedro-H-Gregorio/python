def fibonnaci(quantidade):
    return round((1.61803398875**quantidade - ((1-1.61803398875)**quantidade))/5**(1/2))

while True:
    n = int(input())
    if n<0:
      break
    print(fibonnaci(n))

"""
A diferença dessa forma para a segunda que está no arquivo 6_quest_forma_2.py é que essa pode fazer até a 1474, já a outra é ineficiente para posições altas pois há uma demora muito grande para as respostas
"""