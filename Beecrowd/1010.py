linhas= []
for i in range(2):
    linhas.append(list(map(float,input().split(" "))))
def reduce(lists, acu):
    for list in lists:
        acu += list[1]*list[2]
    return acu
print("VALOR A PAGAR: R$ %.2f"%(reduce(linhas,0)))