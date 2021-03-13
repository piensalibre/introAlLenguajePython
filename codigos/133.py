#codigo 133, repaso
print("Proporciona los siguientes datos del libro:")
nombre = input("Proporciona el nombre: ")
id = int(input("Proporciona el id: "))
precio = float(input("Ingresa el precio: "))
envioGratuito = input("Indica si el envio es gratuito (True/False): ")
if envioGratuito == "True":
    envioGratuito = True
elif envioGratuito == "False":
    envioGratuito = False
else:
    envioGratuito = "Valor incorrecto, debe ser True o False"
print("Nombre:",nombre)
print("Id:",id)
print("Precio:",precio)
print("Envio gratuito:",envioGratuito)
