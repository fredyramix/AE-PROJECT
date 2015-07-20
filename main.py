__author__ = 'jramirez'
import random
from convertirfechas import convertir
from graficadora import graficar

TAM_POBLACION=20
m=1 #numero de variables.
TAM_INDIVIDUO=2
def leerfechas():
    f=open("archivos_de_configuracion/datosconvertidos.txt","w")
    fo = open("archivos_de_configuracion/datos.txt", "r")
    configuracion= [linea.split() for linea in fo.readlines()]
    fo.close()

    fo = open("archivos_de_configuracion/magnitudes.txt", "r")
    mag= [linea.split() for linea in fo.readlines()]
    fo.close()

    fo = open("archivos_de_configuracion/latitud_longitud.txt", "r")
    lat_long= [linea.split() for linea in fo.readlines()]
    fo.close()

    for i in range(0,len(configuracion)):
        cadena= configuracion[i][0]+" "+configuracion[i][1]
        convertir(cadena,f,mag[i][0],lat_long[i])
    f.close()
def crearPoblacion(tam_indi,tam_pob):
    poblacion=[]
    for i in range(tam_pob):
        individuo=[]
        for j in range(tam_indi):
            individuo.append(random.randint(0,10))
        poblacion.append(individuo)
    return poblacion
def H(x):
    pass
def I(x):
    pass
def calcularAptitud(pob):
    #magnitud_estimada=

    aptitud = (1/(2*m))

    for i in range(1,m):
        pow((H(x)-I(x)),2)
def main():
    #leerfechas()
    #graficar()

    poblacion=crearPoblacion(TAM_INDIVIDUO,TAM_POBLACION)

    #una vez creado los valores de Teta aleatorios sigue evaluar.

    aptitud=calcularAptitud(poblacion,m)


main()