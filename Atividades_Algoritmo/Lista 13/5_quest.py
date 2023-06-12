nomes = []
for i in range(10):
    nomes.append(input())
nomes.sort()
print("\n".join(map(str,nomes)))