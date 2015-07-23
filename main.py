from funcionAptitud import calcularAptitud

__author__ = 'jramirez'
import random
from cruzamiento import cruzar
from graficadora import *
from seleccionamejor import elitismo
from mutacion import mutar
from salida import escribir
from seleccion import seleccionar,seleccionarMejores
TAM_POBLACION=10
import time

#m=3 #numero de variables.
TAM_INDIVIDUO=2

def crearPoblacion(tam_indi,tam_pob):
    poblacion=[]
    for i in range(tam_pob):
        individuo=[]
        for j in range(tam_indi):
            #individuo.append(random.uniform(0.000000001,0.000000002))
            individuo.append(random.uniform(1,10))
        poblacion.append(individuo)
    return poblacion


def leerDatos():
    fo = open("archivos_de_configuracion/datosconvertidos.txt", "r")
    data= [linea.split(",") for linea in fo.readlines()]
    fo.close()
    for i in range(len(data)):
        aux=data[i][-1][-5:-1]
        data[i][-1]=float(aux)
    return data

def generarPuntosMejor(mejor,muestras):
    x=[]
    y=[]
    x1=muestras[0][0] #punto inicial
    x.append(x1)
    x2=muestras[-1][0] #punto final
    x.append(x2)
    suma=float(mejor[0][0])
    for i in range(1,len(mejor[0])):
        suma+=float(mejor[0][i])*float(x1)
    y.append(suma)
    #print suma
    suma=0
    for i in range(1,len(mejor[0])):
        suma+=float(mejor[0][i])*float(x2)
    y.append(suma)
    #print suma
    return x,y


def main(start_time):
    g=0
    outfile=open("Resultados/salida.txt",'w')
    #bandera = False #bandera para saber cuando se va mejorando la raza
    mejor = [] #nuestro mejor individuo.
    mejor.append(-1)
    mejor.append(-1)
    #leerfechas()
    #graficar()
    muestras=leerDatos()
    n = len(muestras)
    #print "numero de muestras: " +str(n)
    '''Los datos estan compuestos por Tiempo,latitud,longitud,magnitud '''
    padres=crearPoblacion(TAM_INDIVIDUO,TAM_POBLACION)
    #una vez creado los valores de Teta aleatorios sigue evaluar.
    aptitud_padres=calcularAptitud(padres,n,muestras)
    #nos devuelve una lista de aptitudes.
    mejor,bandera = elitismo(padres,aptitud_padres,mejor)

    selecionados=seleccionar(padres,aptitud_padres)

    a="El mejor hasta ahora:"
    escribir(outfile,a)
    a= "Generacion: " +str(g)
    escribir(outfile,a)
    a= "Vector: "+str(mejor[0])
    escribir(outfile,a)
    a="Aptitud: "+str(mejor[1])
    escribir(outfile,a)
    a="Tiempo: " +str(time.time()-start_time)+" segundos"
    escribir(outfile,a)
    #x,y=generarPuntosMejor(mejor,muestras)
    #graficar(x,y)

    '''Proceso de cruza'''
    hijos=cruzar(selecionados)
    aptitud_hijos=calcularAptitud(hijos,n,muestras)
    '''Seleccionar mejores entre padres e hijos'''
    mejores=seleccionarMejores(padres,hijos,aptitud_padres,aptitud_hijos)
    mutados = mutar(mejores)
    aptitud_padres=calcularAptitud(mutados,n,muestras)

    mejor,bandera = elitismo(mutados,aptitud_padres,mejor)
    padres=mutados[:]
    g=1
    while True:
        selecionados=seleccionar(padres,aptitud_padres)
        hijos=cruzar(selecionados)
        aptitud_hijos=calcularAptitud(hijos,n,muestras)
        '''Seleccionar mejores entre padres e hijos'''
        mejores=seleccionarMejores(padres,hijos,aptitud_padres,aptitud_hijos)
        mutados = mutar(mejores)
        aptitud_padres=calcularAptitud(mutados,n,muestras)
        mejor,bandera = elitismo(mutados,aptitud_padres,mejor)
        padres=mutados[:]
        #print aptitud
        if bandera==True:
            a="El mejor hasta ahora:"
            escribir(outfile,a)
            a= "Generacion: " +str(g)
            escribir(outfile,a)
            a= "Vector: "+str(mejor[0])
            escribir(outfile,a)
            a="Aptitud: "+str(mejor[1])
            escribir(outfile,a)
            a="Tiempo: " +str(time.time()-start_time)+" segundos"
            escribir(outfile,a)
            x,y=generarPuntosMejor(mejor,muestras)
            graficar(x,y)
        g+=1
start_time = time.time()
main(start_time)