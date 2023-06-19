class Fila:

    def __init__(self):
        self.data = []

    def add(self , value):
        return self.data.append(value)
    
    def pop(self):
        return self.data.pop(0)
    
    def count(self):
        return len(self.data)
    
    def find(self,value):
        return self.data.index(value)
    
    def list(self):
        return [print(i,sep="\n") for i in self.data]
    
    def isEmpty(self):
        return self.count() == 0 and True or False
    
pacientes = Fila()
pacientesPrioritarios = Fila()
controle = False

def verificaPrioridade():
    classificacao = input("É prioridade?: (s/n) ")
    return classificacao == "s" and True or False


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
           if verificaPrioridade():
               pacientesPrioritarios.add(input("Digite o nome do paciente para adicionar: "))
               controle = True
           else: 
                pacientes.add(input("Digite o nome do paciente para adicionar: "))
        case "2":
            print("Pacientes prioritários :")
            pacientesPrioritarios.list()
            print("Pacientes sem prioridade :")
            pacientes.list()
        case "3":
            if pacientesPrioritarios.isEmpty():
                pacientes.pop()
            elif controle:
                pacientesPrioritarios.pop()
                controle = False
            else: 
                pacientes.pop()
                controle = pacientesPrioritarios.isEmpty() and True or False

        case "5":
            if verificaPrioridade():
                print(pacientesPrioritarios.find(input("Digite o nome do paciente que quer procurar: ")))
            else: 
                print(pacientes.find(input("Digite o nome do paciente que quer procurar: ")))
        case "4":
            print("Pacientes prioritários :", pacientesPrioritarios.count())
            print("Pacientes sem prioridade :", pacientes.count())
            print("Pacientes Totais:",pacientes.count()+ pacientesPrioritarios.count())
        case "6":
            break