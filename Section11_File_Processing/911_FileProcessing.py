# ABRIR ARCHIVOS EN DIFERENTES DIRECTORIOS
with open("FILES/vegetables.txt", "w") as myfile:
    content = myfile.write("Tomato")

# Esribir texto en un archivo
# Al abrir el archivo debemos indicar los permisos con los que abrimos el mismo.
#   abrir en la ayuda de python -help(open)- para documentación

# Si abrimos un archivo con permiso de escritura "w" y escribimos directamente en él,
#   lo que haremos es sobreescribir el archivo completamente, perdiendo los datos anteriores
#   si lo que queremos es añadir una linea al principio debemos usar "\n" tras el texto a incluir
with open("FILES/copy_from_fruits.txt", "w") as myfile:
    content = myfile.write("Tomato\nCucumber\nOnion")
# Si usamos más de un método debemos tener cuidado donde vamos a escribir, puesto que podríamos 
#   escribir en la misma linea, a continueación de lo último.
    content = myfile.write("\nGarlic")
