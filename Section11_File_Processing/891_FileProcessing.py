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
myfile.close()
print (content)
# Es necesario cerrar el archivo y eliminar el objeto de la RAM para liberar memorira tras procesar el archivo.


# Una forma mejor de manejar los archivos es con el WITH CONTEXT MANAGER
#   el método WITH maneja completamente el objeto, por lo que no es necesario cerrarlo con CLOSE()
with open("fruits.txt") as myfile:
    content = myfile.read()

print (content)
