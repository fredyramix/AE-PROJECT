__author__ = 'freddy'
import random
def mutar(cruzados):
    #print "Tamano de Poblacion: "+str(len(cruzados))
    x = random.randint(0,len(cruzados)-1)
    #print "numero de invididuo: "+str(x)
    muta= cruzados[x]
    #print "Individuo: "+str(muta)
    y = random.randint(0,len(muta)-1)
    #print "posicion individuo: "+str(y)
    #print "el que se va a mutar: "+str(muta[y])
    #print "Tamano Individuo: "+str(tam)
    mut = random.uniform(0.000000001,1)
    #print "Nuevo numero:" +str(mut)
    #print cruzados[x][y]

    #print "==========================="

    cruzados[x][y]=mut

    #print cruzados[x][y]
    #raw_input("aaaaaaaaaaaaaaaaaaaaa")
    #print cruzados
    return cruzados