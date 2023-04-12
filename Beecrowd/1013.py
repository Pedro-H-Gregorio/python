n = list(map(int,input().split(" ")))

def maior(a,b):
    return (a+b+abs(a-b))/2

print(f"{maior(maior(n[0],n[1]),n[2]):.0f} eh o maior")