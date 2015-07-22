__author__ = 'freddy'

import time

def convertir(date_time,f,magnitud,lat_long):
    #date_time = '29.08.2011 11:05:02'
    pattern = '%d.%m.%Y %H:%M:%S'
    epoch = int(time.mktime(time.strptime(date_time, pattern)))
    f.write(str(epoch))
    f.write(","+str(lat_long[0])+","+str(lat_long[1]))
    f.write(","+str(magnitud))
    f.write("\n")