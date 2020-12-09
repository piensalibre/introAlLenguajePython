#codigo 31, ejemplo de codigo que importa como un modulo el codigo del archivo 31.py
import modulo as md#con la palabra reservada import se importa el modulo "modulo.py" y mediante la palabra reservada "as" se asigna un alias de igual manera se puede seleccionar lo que se va a importar del modulo, por ejemplo si se deseara importar unicamente la funcion saludo se haria de la siguiente manera "from modulos import saludo", al importar de esa manera ya no es necesario llamar la funcion desde el modulo, se puede llamar directamente

print(md.mascotas)#para usar el modulo se usa el nombre o alias del modulo mas el ".", seguido de la funcion o de lo que se desee usar de dicho modulo
md.saludo("Piensa")