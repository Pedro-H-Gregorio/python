while True:
    numbers = list(map(int,input().split()))
    if numbers[0]>numbers[1]:
        print("Decrescente")
    elif numbers[0]<numbers[1]:
        print("Crescente")
    else: break