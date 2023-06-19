class Fila:

    def __init__(self):
        self.data = []

    def add(self , value):
        return self.data.append(value)
    
    def pop(self, value):
        return self.data.pop(0)
    
    def count(self):
        return len(self.data)
    
    def find(self,value):
        return self.data.index(value)
    
    def list(self):
        return [print(i,sep="\n") for i in self.data]


pacientes = Fila()

while True :
    escolha = input("\n\n-----------------\n"
        " - > Menu < -\n"
        "-----------------\n"
        "1 - Adicionar paciente\n"
        "2 - Listar pacientes\n"
        "3 - Proximo paciente\n"
        "4 - Mostrar quantidade de pacientes\n"
        "5 - Procurar posição do paciente\n"
        "6 - Sair\n\n")

    match escolha:
        case "1":
           pacientes.add(input("Digite o nome do paciente para adicionar: "))
        case "2":
            pacientes.list() 
        case "3":
            print(pacientes.pop())
        case "5":
            print(pacientes.find(input("Digite o nome do paciente que quer procurar: ")))
        case "4":
            print(pacientes.count())
        case "6":
            break