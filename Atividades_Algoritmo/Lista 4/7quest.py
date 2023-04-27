ano = int(input())
if (ano%400 ==0) or (ano%4==0) and not (ano%100==0):
    print(f'{ano} é bissexto!')
else: print(f"{ano} não é bissexto!")
