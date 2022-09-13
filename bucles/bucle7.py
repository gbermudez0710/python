#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
#forma 1
numero=1
for i in range(numero,11,1):
    for j in range(11):
        print("la tabla del numero " , i , " es :",i, "x ",j," : ",j*i)        

#forma2
#for i in range(1, 11):
#    for j in range(1, 11):
#        print(i*j, end="\t")
#    print("")