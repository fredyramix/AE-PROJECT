__author__ = 'freddy'
import random
def seleccionar(poblacion,aptitudes):
    seleccionados=[]
    for i in range(len(poblacion)):
        posicion1=random.randint(0,len(poblacion)-1)
        preseleccionad1=aptitudes[posicion1]
        preseleccionad1_indi=poblacion[posicion1]
        posicion2=random.randint(0,len(poblacion)-1)
        preseleccionado2=aptitudes[posicion1]
        preseleccionad2_indi=poblacion[posicion2]

        seleccionado = torneo(preseleccionad1,preseleccionad1_indi,preseleccionado2,preseleccionad2_indi)
        #print seleccionado
        #raw_input("aaaaaaaaaa")
        seleccionados.append(seleccionado)
    return seleccionados

def torneo(ap1,v1,ap2,v2):
    if ap1<ap2:
        return v1
    else:
        return v2

def seleccionarMejores(padres,hijos,aptitud_padres,aptitud_hijos):
    mejores=[]

    for i in range(len(padres)):
        padres[i].append(aptitud_padres[i])
        hijos[i].append(aptitud_hijos[i])

    lista=padres+hijos
    lista.sort(key=lambda x:x[-1]) #ordenamos la lista por menores aptitudes.

    for i in range(len(padres)):
        mejores.append(lista[i])
    for j in mejores:
        del j[-1]
    return mejores