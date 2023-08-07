lista = []
lista_1 = list()

#adiciona um item;
lista.append(1)
lista.insert(2,1)
 
#resgata um item ou a lista
lista[0]
lista.copy()
lista.index(0,1)

#deleta
del lista[0]
lista.remove(1)
lista.clear()

#operações
lista.sort() #ordena
lista.reverse() #inverte a ordem
lista_2 = [i for i in lista]

#Podem ser aplicados os mesmos metodos para tuplas. a diferença é que não pode inserir depois de criada
tupla = tuple()
