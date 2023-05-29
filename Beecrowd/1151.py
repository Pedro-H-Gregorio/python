def fibonnati(quantidade):
    sequencia = [0,1]

    for i in range(1,quantidade-1):
          sequencia.append(sequencia[-1]+sequencia[-2])
    return sequencia


n = int(input())
print(" ".join(list(map(str,fibonnati(n)))))