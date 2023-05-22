number = int(input())
eh_primo = True

for i in range(2,number):
    if number % i == 0:
        eh_primo = False
        break

print( eh_primo and 'É primo'or'Não é primo')