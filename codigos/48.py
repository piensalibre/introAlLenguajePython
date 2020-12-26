#codigo 48, ejemplo de funcion que imprime el saludo dependiendo el argumento que reciba
def saludo(lang):
    if lang == "es":
        print("Hola")
    elif lang == "fr":
        print("Bonjour")
    else:
        print ("Hello")

saludo("es")
saludo("fr")
saludo("en")