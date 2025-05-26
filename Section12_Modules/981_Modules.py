import time
import os
import pandas

while True:
    if os.path.exists("FILES/temps_today.csv"):
        data = pandas.read_csv("FILES/temps_today.csv")
        #print (data.mean())                                 # Media de cada una de las columnas
        print (data.mean() ["st1"])                         # Media de la primera columna, que en el archivo se llama "st1"
    else:
        print ("File does not exists.")
    time.sleep(10)