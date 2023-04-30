n1, n2, n3, n4 = map(int, input().split())

mf = n4 - n2
hf = n3 - n1

if n4 == n2 and n1 == n3:
    print(f"O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
    if mf < 0:
        hf -= 1
        mf += 60
    if hf < 0:
        hf += 24
    print(f"O JOGO DUROU {hf} HORA(S) E {mf} MINUTO(S)")

