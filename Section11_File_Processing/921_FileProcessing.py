# AÑADIR TEXTO A UN ARCHIVO EXISTENTE
with open("FILES/copy_from_fruits.txt", "a+") as myfile:
    # El permiso "a" permite abrir para escribir y añadir al final del archivo si existe "a" = APPEND
    myfile.write("\nOkra")
    # Tras la escritura colocamos el cursor de nuevo antes del primer caracter de la primera linea
    myfile.seek(0)
    # El permiso "a+" permite tanto escribir como leer (ver help(open))
    content = myfile.read()

print(content)
    
