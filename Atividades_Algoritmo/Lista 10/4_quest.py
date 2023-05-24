string1 = input()
string2 = input()
string1, string2 = sorted([string1,string2])
substring = ""
controle = 0

for i in range(len(string1)):

    if string1[controle:i+1] in string2:
        if len(substring)<len(string1[controle:i+1]):
            substring=string1[controle:i+1]
        continue
    controle=i+1

    
print(len(substring))
