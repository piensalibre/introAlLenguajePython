#codigo 32, ejemplo de lectura de archivos
p = open("piensa.txt","r")#hacemos uso de la funcion open, la cual recibe como argumento la direccion del archivo y el modo o permiso de la apertura del archivo, el modo por defecto es el de leer 'r', tambien existe el modo append 'a', que es el de agregar caracteres al archivo, tambien existe el archivo write 'w', el cual si no existe el archivo lo crea y si ya existe lo sobreescribe por completo, tambien existe el archivo para crear 'x', este permiso solo devuelve error si ya existe el archivo
print(p.read())#el metodo read lee donde apunta 'p' de manera corrida, de inicio a fin