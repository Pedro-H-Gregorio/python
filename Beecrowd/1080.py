cont = 0
index = 0
for i in range(1,5):
    number = int(input())
    if cont<=number:
        cont = number
        index = i
        
print(cont)
print(index)