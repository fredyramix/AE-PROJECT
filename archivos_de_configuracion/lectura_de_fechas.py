__author__ = 'freddy'
from convertirfechas import convertir
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