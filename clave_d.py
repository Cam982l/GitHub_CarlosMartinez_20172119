import math


"""
***************************************************************
@@ ejercicio 1 @@
un metodo python que haga la multiplicacion de 3 numeros
2*4*3 = 24
"""


# start-->
def multiplicar(num1, num2, num3):
        
    result = num1 * num2 * num3
    print(result)
    return result

"""
***************************************************************
@@ ejercicio 2 @@
la suma de los numeros divisibles entre 3 y 5 del 1000 al 2000
"""


# start-->
def sumaDivTresYCincoPlus():
    suma = 0 
    for i in range(1000, 2000):
        if (i % 3 == 0) and (i % 5 == 0): 
            suma += i
    result = suma
    print(suma)
    return suma

    

"""
***************************************************************
@@ ejercicio 3 @@
encontrar el area y el volumen de un ortoedro
longitud = 10 m
latitud = 6 m
altura = 5 m

area: A = 2(longitud · latitud + longitud · altura + latitud · altura)
volumen: V = longitud · latitud · altura
"""


# start-->
def definicionOrtoedro(longitud, latitud, altura):
    area = obtenerArea(longitud, latitud, altura)
    volumen = obtenerVolumen(longitud, latitud, altura)
    result = {'area': area, 'volumen': volumen}
    print(area)
    print(volumen)
    return result

def obtenerArea(longitud, latitud, altura):
    result = 2*(longitud * latitud + longitud * altura + latitud * altura)
    return result


def obtenerVolumen(longitud, latitud, altura):
    result = longitud * latitud * altura
    return result


"""
***************************************************************
@@ ejercicio 4 @@
el ejercicio numero 3 convertirlo en una clase

"""


# start-->
class Ortoedro:
    def definicionOrtoedro(self):
        return 0


"""
***************************************************************
@@ ejercicio 5 @@
VentaComputadoras
Computadora
    procesador
    ram
    tarjeta_grafica
    ssd
    costo
    conDescuento
    descuento
    conPlazo
    cuota
"""


class VentaComputadoras:
    def orden(self):
        pass

    def totalProcesadorIntel(self):
        return 0

    def totalRam16ConDescuento(self):
        return 0


class Computadora:
    pass


"""
***************************************************************
@@ ejercicio 6 @@
colocar este proyecto en github
colocar aca debajo la url
ademas colocar la url en un archivo
github_<nombre>_<codigo>.txt y subirlo a moodle
"""


# github url-->
def getGithubUrl():
    return ""
