#Abrir archivo
myfile = open("fruits.txt")     # Ruta hasta el archivo que queremos abrir
                                # Crea un objeto FILE con el documento abierto

# Mover el cursor
# Cuando se ejecuta el OPEN(), el cursor se coloca al inicio del documento
#   Al ejecutar el READ() el cursor queda en el final del documento,
#   por lo que volver a ejecutar READ() se imprime una linea en blanco (no hay texto para leer)
#   La forma en la que podemos imprimir varias veces es guardar el READ() en una variable 
#   e imprimir la variable
content = myfile.read()
print (content)
print (content)
