number = []
for i in range(10):
    number.append(int(input()))
number.sort(reverse=True)
print(" ".join(map(str,number)))