#codigo 20, ejemplo de for loop
usuarios = ["Piensa","libre","hola","mundo"]

for usuario in usuarios:#este ciclo for itera los items de la lista usuarios y los asigna a usuario
    print(usuario)

usuario = "Piensa libre"

for c in usuario:#este ciclo for itera todos los caracteres de la cadena usuario
    print(c)


for usuario in usuarios:#este ciclo for itera los items de la lista usuarios y los asigna a usuario
    if usuario == "hola":
        break
    print(usuario)