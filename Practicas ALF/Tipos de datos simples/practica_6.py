print("Desea hacer una operación aritmetica")
opc=int(input("1__Si\n2__No"))

if opc == 1:
    while True:
        print("Intoduzca un Numero positivo para hacer la opearción")
        n=int(input())
        if n<=0:
                print("El numero introducido es incorrecto o no es positivo, por favor vuelva a introducirlo")
        else:
            operacion=(n*(n+1))/2
            print(f"El resultado es: {operacion}")
elif opc == 2:
    print("Adiós")
else:
     print("Opción no valida")
