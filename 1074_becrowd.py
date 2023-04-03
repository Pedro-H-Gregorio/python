hi, mi, hf, mf = map(int,input().split())

ht = hf - hi
mt = mf - mi

if ht <= 0 :
    ht += 24
elif mi > mf:
    mt += 60
    ht -= 1

if hf == hi and mi == mf:
    print("O jogador jogou por 24 Horas")
else: print(ht, mt)