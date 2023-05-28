def intervalo(v_i,v_s):
   for i in range(v_i,v_s+1):
      print(i)

while True:
    try:
      v_inferior, v_superior = map(int,input().split())
      if [v_inferior,v_superior].count(0) == 2:
         raise ValueError("Encerrado")
      intervalo(v_inferior,v_superior) 
    except:
        break