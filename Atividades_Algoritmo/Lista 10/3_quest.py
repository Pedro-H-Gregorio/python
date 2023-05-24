while True:
    numbers = list(map(float,input().split()))
    if numbers.count(0) == 2:
        break
    else: print(numbers[0]*numbers[1])