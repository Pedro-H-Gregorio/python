mes = input().lower()

match mes:
    case "janeiro"| "março" | "maio" | "julho" | "agosto" | "outubro" | "dezembro":
        print("Tem 31 dias")
    case "abril" | "junho" | "setembro" | "novembro":
        print("Tem 30 dias")
    case "fevereiro":
        print("Tem 28 dias")