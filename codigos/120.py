#codigo 120, ejemplo de como extraer cadenas usando un doble split
x = 'De piensa@libre para ti'
palabras = x.split(" ")
email = palabras[1]
emailPartes = email.split('@')
print(emailPartes[1])