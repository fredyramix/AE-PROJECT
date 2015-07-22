__author__ = 'freddy'
def H(muestra,indi):
    tetax=0
    for i in range(len(indi)):
        if i == 0:
            #print indi[i]
            tetax+=float(indi[i])
            #raw_input("bbbbb")
        else:
            #print indi[i]
            #print muestra[1]
            #raw_input("ccccccccccccc")
            tetax+=float(indi[i])*float(muestra[1])
    return tetax

def I(muestra):
    #print muestra[-1]
    #raw_input("aaaaaa")
    return float(muestra[-1]) #que vendria siendo la magnitud de esa muestra.
def sumatoria(indi,n,muestras):
    suma=0
    for i in range(n):
        suma += (pow((H(muestras[i],indi)-I(muestras[i])),2))
    return suma
def calcularAptitud(pob,n,muestras):
    aptitudes=[]
    factor= float((1.0/(2*float(n))))
    for individuo in pob:
        sumatori =float(sumatoria(individuo,n,muestras))
        aptitud=factor * sumatori
        #print "sumatoria= "+str(sumatori)
        #print "factor= " + str(factor)
        #print aptitud
        #raw_input("wait...")
        aptitudes.append(aptitud)
    return aptitudes