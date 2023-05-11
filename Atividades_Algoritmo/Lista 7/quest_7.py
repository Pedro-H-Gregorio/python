from functools import reduce
print(reduce(lambda x,b: x+b,range(100,401,2),0))