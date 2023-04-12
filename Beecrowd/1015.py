n1 = list(map(float,input().split(" ")))
n2 = list(map(float,input().split(" ")))

print(f'{((((n1[0]-n2[0])**2)+((n1[1]-n2[1])**2))**(1/2)):.4f}')