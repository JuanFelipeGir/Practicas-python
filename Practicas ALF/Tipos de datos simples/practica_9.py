inversion=float(input("Ingrese la cantidad que desea invertir: "))
interes=float(input("Ingrese el porcentaje de interés anual: "))
años=int(input("Ingrese la cantidad de años: "))
capital_obtenido = inversion * (1 + (interes / 100)) ** años
print(f"El capital obtenido en {años} es igual a {capital_obtenido}")