while True:
    try :
        text = input().upper()
        fraseNova = ""
        eh_maiuscula = True
        for i in text:
            if i != " ":
                if eh_maiuscula:
                    fraseNova += i
                    eh_maiuscula = False
                else:
                    fraseNova += i.lower()
                    eh_maiuscula = True
            else:
                fraseNova += i

        print(fraseNova)
    except EOFError:
        break