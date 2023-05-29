number = int(input())
contIn = 0
contOut = 0
for i  in range(number):
    numberInt = int(input())
    if numberInt>=10 and numberInt<=20: 
        contIn+=1
    else:
        contOut+=1


print(f'{contIn} in')
print(f'{contOut} out')