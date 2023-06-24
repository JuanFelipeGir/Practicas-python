def calcularAVG (numeros):
    suma=sum(numeros)
    cant=len(numeros)
    promedio=suma/cant
    return promedio

numeros=[10,20,30]
result=calcularAVG(numeros)
print(f"El resultado del promedio es:{result}")