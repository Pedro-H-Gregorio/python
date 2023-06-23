from Alunos import Alunos

alunos = Alunos()

while True :
    escolha = input("\n\n-----------------\n"
        " - > Menu < -\n"
        "-----------------\n"
        "1 - Adicionar Aluno\n"
        "2 - Listar Alunos\n"
        "3 - Excluir Aluno\n"
        "4 - Atualizar Aluno\n"
        "5 - Quantidade de alunos\n"
        "6 - Sair\n\n")
    
    match escolha:
        case "1":
            alunos.add(*list(map(input,["Nome: ","Data de Nascimento: ","Ano de ingresso: "])))
        case "2":
            alunos.list()
        case "3":
            alunos.remove(input("Digite a matricula do aluno que quer remover: "))
        case "4":
            matricula = input("Digite a matricula do aluno que quer atualizar: ")
            propriedade = {"nome":"nome", "data de nascimento": "dtNascimento", "ano de ingresso": "anoIngresso"}
            opcao = input("O que deseja atualizar? (Nome, Data de Nasicimento, Ano de ingresso) ").lower().strip()
            value = input("Informe o(a) "+opcao+": ")
            alunos.update(matricula,{propriedade[opcao]:value})
        case "5":
            print(f'Existem: {alunos.count()} Alunos')
        case "6":
            break
