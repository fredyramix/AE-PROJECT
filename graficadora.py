import matplotlib.pyplot as plt
import numpy as np

def graficar():
    fo = open("archivos_de_configuracion/datosconvertidos.txt", "r")
    listilla= [linea.split(",") for linea in fo.readlines()]
    fo.close()
    x=[]
    y=[]
    for i in listilla:
        print i
        x.append(int(i[0]))
        y.append(float(i[-1]))

    plt.plot(x,y, marker='x', linestyle=':', color='b', label = "Enero")
    plt.xlabel("time(s)")
    plt.ylabel("Magnitud")
    plt.show()


