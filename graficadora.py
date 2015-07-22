import matplotlib.pyplot as plt
import numpy as np

def graficar(x1,y1):
    fo = open("archivos_de_configuracion/datosconvertidos.txt", "r")
    listilla= [linea.split(",") for linea in fo.readlines()]
    fo.close()
    x=[]
    y=[]
    for i in listilla:
        x.append(int(i[0]))
        y.append(float(i[-1]))
    plt.plot(x,y, marker='x', linestyle=':', color='b')
    plt.plot(x1,y1, marker='o', linestyle='--', color='r')
    plt.xlabel("time(s)")
    plt.ylabel("Magnitud")
    plt.show()


def graficarRecta(x,y):
    plt.plot(x,y, marker='o', linestyle='--', color='r', label = "Marzo")
    plt.show()
    #raw_input("aaaaaaaaaa")


