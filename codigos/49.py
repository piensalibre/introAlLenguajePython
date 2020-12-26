#codigo 49,ejemplo de funcion que retorna el saludo dependiendo el argumento que reciba
def saludo(lang):
    if lang == "es":
        return "Hola"
    elif lang == "fr":
        return "Bonjour"
    else:
        return "Hello"

print(saludo("en"),"Piensa")
print(saludo("es"),"libre")