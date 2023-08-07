conjunto = set("abracadabra")

conjunto.add("pedro")
new_role = conjunto.union(set("pedro"))


print(conjunto)
print(new_role)
print(new_role.difference(conjunto))
conjunto.update("oiee")
print(conjunto)
conjunto.remove("i")
conjunto.add("p")
print(conjunto == new_role)
print(sorted(conjunto))
print(sorted(new_role))
new_role.add("5")
print(conjunto.isdisjoint(new_role))