class Pilha:

    def __init__(self):
        self.data = []

    def add(self , value):
        return self.data.append(value)
    
    def pop(self):
        return self.data.pop()
    
    def count(self):
        return len(self.data)
    
    def find(self,value):
        return self.data.index(value)
    
    def list(self):
        return [print(i,sep="\n") for i in self.data]

pecas = Pilha()

while True :
    escolha = input("\n\n-----------------\n"
        " - > Menu < -\n"
        "-----------------\n"
        "1 - Adicionar peça\n"
        "2 - Listar peças\n"
        "3 - Tirar peça\n"
        "4 - Mostrar quantidade de peças\n"
        "5 - Procurar peça\n"
        "6 - Sair\n\n")

    match escolha:
        case "1":
           pecas.add(input("Digite a peça para adicionar: "))
        case "2":
            pecas.list() 
        case "3":
            print("Peça removida:",pecas.pop())
        case "5":
            print(pecas.find(input("Digite a peça que quer procurar: ")))
        case "4":
            print(pecas.count())
        case "6":
            break
