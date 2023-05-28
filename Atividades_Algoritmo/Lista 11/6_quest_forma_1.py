def fibonnaci(quantidade):
    return round((1.61803398875**quantidade - ((1-1.61803398875)**quantidade))/5**(1/2))

while True:
    n = int(input())
    if n<0:
      break
    print(fibonnaci(n))

"""
A diferença dessa forma para a segunda que está no arquivo 6_quest_forma_2.py é que essa pode fazer até a 1474,
já a outra é ineficiente para posições altas pois há uma demora muito grande para as respostas.

Para posições até 50 esse arquivo é bom pois em testes esse demorou 0.330 segundos para excutar, 
ganhando do 6_quest_forma_3.py que ficou com 0.370 em média. Tudo isso com a mesma entrada de testes

Entretanto, essa se mostra ineficiente quanto a exatidão, pois ela trabalha com a formula e arredonda para o numero
mais proximo, se tornando ineficiente para valores grandes, exemplo: 1000. Para que fosse corrigido isso, teria de
aumentar o valor da constante de phi (1.61803398875).
"""