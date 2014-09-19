import datetime
def sabado(fecha):
    dia=datetime.date(fecha.year,fecha.month,fecha.day)
    if (datetime.date.weekday(dia)==5):
        return True
    else:
        return False
  
cfecha = input("Ingrese la fecha (dd/mm/aaaa): ")
dfecha=datetime.datetime.strptime(cfecha, "%d/%m/%Y")
print (sabado(dfecha))

def IMC(peso, estatura):
    IMC = peso/estatura**2
    return print ("Tu IMC es de {}" . format(IMC))
peso = float(input("Teclea tu peso en kilos "))
estatura = float(input("Teclea tu estatura en metros "))
IMC(peso, estatura)


import math
base=float(input("Teclee cuánto mide la base del triángulo rectangulo "))
angulo= math.radians(float(input("Teclee el ángulo en grados")))
cateto=input("¿El ángulo es adyacente u opuesto a la base?(opuesto/adyacente) ")
if cateto == "opuesto":
    angulo=90-angulo
tan=math.tan(angulo)
print("El cateto mide {} " .format(tan*base))

