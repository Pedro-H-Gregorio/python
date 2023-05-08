numero_da_semana = input()

match numero_da_semana:
    case "1" | "7":
        print("Não é útil")
    case "2" | "3" | "4" | "5" | "6":
        print("É útil")