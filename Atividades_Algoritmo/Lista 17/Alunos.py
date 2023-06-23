from Aluno import Aluno

class Alunos:
    
    def __init__(self):
        self.alunos = []
    
    def findIndex(self ,matricula):
        return next(i for i in range(len(self.alunos)) if self.alunos[i].getAluno()["matricula"] == matricula)

    def calculaMatricula(self):
         if self.count() == 0:
             return 1
         else: 
            return int(self.alunos[-1].getAluno()["matricula"])+1
    
    def count(self):
        return len(self.alunos)
    
    def list(self):
        return [print("-------------------",i,"-------------------",sep="\n") for i in self.alunos]

    def add(self,nome,dtNascimento,anoIngresso):
        return self.alunos.append(Aluno(str(self.calculaMatricula()),nome,dtNascimento,anoIngresso))
    
    def remove(self,matricula):
        return self.alunos.pop(self.findIndex(matricula))
    
    def update(self,matricula,obj):
        return self.alunos[int(self.findIndex(matricula))].upsert(obj)