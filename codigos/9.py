#codigo nueve, mas sobre diccionarios se estudian casos de diccionarios anidados

piensalibre = {
        "nombre":"piensalibre",
        "apellido":"libre"
        }

persona = {
        "piensa":{#se le asigna un diccionario como valor a la llave, se crea un diccionario anidado
            "nombre":"piensa",
            "apellido":"libre"
            },
        "libre":{
            "nombre":"libre",
            "apellido":"libre"
            },
        "piensalibre":piensalibre#se agrega el diccionario almacenado en la variable piensalibre como valor a la llave piensalibre del diccionario persona
        }

print(persona)

humano = dict(nombre = "humano",apellido = "libre")#se crea diccionario con la funcion dict

print(humano)
