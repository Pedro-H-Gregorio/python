memoria = ['load 6', 'add 7', 'store 6', 'jump 1', 0, 0, 1,1]

pc = 0
acumulador = 0
while pc<2:
    busca = memoria[pc].split()
    match busca[0]:
        case 'load' | 'add':
            acumulador += memoria[int(busca[1])]
        case 'store':
            memoria[int(busca[1])] = acumulador
        case 'jump':
            pc = int(busca[1]) - 1
    pc += 1

a = 0
while True:
    a+=1