class Aluno:
    def __init__(self, matricula, nome, dtNascimento, anoIngresso):
        self.aluno = {
            "matricula": matricula,
            "nome": nome,
            "dtNascimento": dtNascimento,
            "anoIngresso": anoIngresso
        }

    def __str__(self):
        return "\n".join([": ".join(
                [str(key), str(values)])
                    for key, values in 
                        dict(
                            zip(
                                ["Matricula", "Nome", "Data de Nascimento", "Ano de ingresso"]
                                , [values for values in self.aluno.values()])).items()])
    
    def upsert(self,obj):
        self.aluno.update(obj)
        return "Foi atualizado com sucesso!"
    
    def getAluno(self):
        return self.aluno
    
