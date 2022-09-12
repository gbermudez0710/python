inversion=float(input("digite la cantidad a invertir: "))
interes=float(input("Digite el interes anual:"))
años=int(input("digite el numero de años: "))
for i in range(años):
    inversion =inversion*1+interes /100
    print("capital tras  "+ str(i+1) + " años: "+ str(round(inversion,2)))