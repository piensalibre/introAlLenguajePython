#codigo 146, repaso
planetas = {"Marte","Jupiter","Venus"}
print(planetas)
print(len(planetas))
print("Marte" in planetas)
planetas.add("Tierra")
print(planetas)
planetas.add("Tierra")
print(planetas)
planetas.remove("Tierra")
print(planetas)
planetas.discard("Jupiter")
print(planetas)
planetas.discard("Saturno")
print(planetas)
planetas.clear()
print(planetas)
del planetas
print(planetas)#Da error porque la variable ya se elimino