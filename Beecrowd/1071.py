numberMaxim = int(input())
numberMin = int(input())
cont = 0
for i  in range(numberMin+1,numberMaxim):
    if i%2 != 0:
        cont+=i

print(cont)