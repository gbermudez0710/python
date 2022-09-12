#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
key = "0710"
password =""
while password != key:
    password = input("Introduce la contraseña: ")
print("Contraseña correcta")