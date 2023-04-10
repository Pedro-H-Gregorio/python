hi, mi, hf, mf = map(int,input().split())

ht = hf - hi
mt = mf - mi

if mi > mf or mt < 0:
    mt += 60
    ht -= 1
if ht < 0 :
    ht += 24

if hf == hi and mi == mf:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else: print(f"O JOGO DUROU {ht} HORA(S) E {mt} MINUTO(S)")