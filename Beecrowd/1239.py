while True:
    try:
        text = input()
        novoTexto = ""
        contI= 0
        contN = 0
        for i in text :
            if i == "_" and contI ==  0:
                i = "<i>"
                contI += 1
            elif i == "_" and contI ==  1:
                i = "</i>"
                contI = 0
            if i == "*" and contN ==  0:
                i = "<b>"
                contN += 1
            elif i == "*" and contN ==  1:
                i = "</b>"
                contN = 0
            novoTexto += i
        print(novoTexto)
    except EOFError:
        break