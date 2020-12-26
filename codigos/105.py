#codigo 105, ejemplo de codigo que ordena listas de tuplas obtenidas de diccionarios por el valor y no por la llave, como extra lo hace de reversa
diccionario = {"uno":1,"dos":2,"tres":3}
temporal = []
for llave,valor in diccionario.items():
    temporal.append((valor,llave))
print(temporal)
temporal = sorted(temporal,reverse=True)
print(temporal)