#Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
p=input("Escriba una palabra: ")
for i in range(len(p)-1,-1,-1):
    print(p[i])