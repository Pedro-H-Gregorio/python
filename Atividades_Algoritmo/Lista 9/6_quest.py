numbers = []

for number in range(200,300+1):
    eh_primo = True

    for i in range(2,number):
        if number % i == 0:
            eh_primo = False
            break

    if eh_primo: numbers.append(number)
    number += 1

print("\n".join(map(str,numbers)))